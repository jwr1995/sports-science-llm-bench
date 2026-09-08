#!/usr/bin/env python3
"""Run the sports-science exam benchmark against one or more local models,
optionally with the context.md reference material, optionally both ways.

Examples:
    uv run python run_exam.py                              # every model, both with and without context
    uv run python run_exam.py --models qwen3-30b-a3b        # one model, both conditions
    uv run python run_exam.py --context with                # only the with-context condition
    uv run python run_exam.py --questions critical_power_model,minetti_descent

Requires:
    - Ollama running locally with the candidate models pulled (see models.py)
    - `uv` installed (syncs dependencies from pyproject.toml automatically)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

from grading import grade
from models import CANDIDATES
from questions import QUESTIONS
from runner import run_question, warm_up

RESULTS_DIR = Path(__file__).resolve().parent / "results"


def _select(items, names, key):
    if not names:
        return items
    wanted = {n.strip() for n in names.split(",")}
    selected = [i for i in items if i[key] in wanted]
    missing = wanted - {i[key] for i in selected}
    if missing:
        sys.exit(f"unknown {key}: {sorted(missing)}")
    return selected


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", help="comma-separated model names from models.py (default: all)")
    ap.add_argument("--questions", help="comma-separated question ids from questions.py (default: all)")
    ap.add_argument("--context", choices=["both", "with", "without"], default="both",
                     help="which context condition(s) to run (default: both)")
    args = ap.parse_args()

    models = _select(CANDIDATES, args.models, "name")
    questions = _select(QUESTIONS, args.questions, "id")
    conditions = {"both": [False, True], "with": [True], "without": [False]}[args.context]

    run_dir = RESULTS_DIR / datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)

    summary_rows = []
    for model_cfg in models:
        for use_context in conditions:
            label = f"{model_cfg['name']}{'+context' if use_context else ''}"
            print(f"\n=== {label} ===")
            print("  (warming up...)", end="", flush=True)
            t0 = time.monotonic()
            warm_up(model_cfg)
            print(f" {round(time.monotonic() - t0, 1)}s")

            records = []
            for q in questions:
                print(f"  {q['id']:<28}", end="", flush=True)
                trace = run_question(model_cfg, q, use_context)
                result = grade(q, trace["answer"])
                records.append({"question": q, "trace": trace, "score": result})
                flags = f" flags={result['red_flags_triggered']}" if result["red_flags_triggered"] else ""
                print(f" coverage={result['coverage']:.0%}{flags}  ({trace['wall_time_s']}s)")

            out_path = run_dir / f"{label.replace('+', '_')}.json"
            out_path.write_text(json.dumps(records, indent=2, default=str))
            summary_rows.append(_summarise(label, records))

    print(f"\nresults written to {run_dir}")
    _print_summary(summary_rows)
    return 0


def _summarise(label: str, records: list) -> dict:
    n = len(records)
    errors = sum(1 for r in records if r["trace"].get("error"))
    avg_coverage = round(sum(r["score"]["coverage"] for r in records) / n, 2) if n else 0.0
    total_flags = sum(len(r["score"]["red_flags_triggered"]) for r in records)
    avg_time = round(sum(r["trace"]["wall_time_s"] for r in records) / n, 1) if n else 0.0
    return {"label": label, "n": n, "avg_coverage": avg_coverage, "red_flags": total_flags,
            "avg_time_s": avg_time, "errors": errors}


def _print_summary(rows: list) -> None:
    print(f"\n{'model (context)':<42}{'avg coverage':<14}{'red flags':<11}{'avg s/q':<9}{'errors'}")
    for r in rows:
        print(f"{r['label']:<42}{r['avg_coverage']:<14}{r['red_flags']:<11}{r['avg_time_s']:<9}{r['errors']}")


if __name__ == "__main__":
    raise SystemExit(main())
