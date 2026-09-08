"""Runs one exam question against one model, with or without the
context.md reference material prepended to the system prompt. No tools
here — this is a pure knowledge/reasoning benchmark, single-turn.
"""
from __future__ import annotations

import time
from pathlib import Path

from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
CONTEXT_PATH = Path(__file__).resolve().parent / "context.md"

BASE_SYSTEM_PROMPT = (
    "You are being examined at MSc level in Sports Science and Sports Data "
    "Science. Answer rigorously and precisely. Name the relevant established "
    "methodology, model, or researcher where relevant rather than giving "
    "generic advice. Do not pad the answer with filler."
)


def _system_prompt(use_context: bool) -> str:
    if not use_context:
        return BASE_SYSTEM_PROMPT
    reference = CONTEXT_PATH.read_text()
    return (
        f"{BASE_SYSTEM_PROMPT}\n\n"
        "Reference material you may draw on (cite it accurately; don't invent "
        f"sources beyond what's here or what you're confident is real):\n\n{reference}"
    )


def run_question(model_cfg: dict, question: dict, use_context: bool) -> dict:
    client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")
    start = time.monotonic()
    error = None
    answer = ""
    try:
        resp = client.chat.completions.create(
            model=model_cfg["ollama_model"],
            messages=[
                {"role": "system", "content": _system_prompt(use_context)},
                {"role": "user", "content": question["prompt"]},
            ],
            extra_body=model_cfg.get("extra_body") or {},
        )
        answer = resp.choices[0].message.content or ""
    except Exception as e:
        error = str(e)

    return {
        "question_id": question["id"],
        "model": model_cfg["name"],
        "use_context": use_context,
        "answer": answer,
        "wall_time_s": round(time.monotonic() - start, 2),
        "error": error,
    }


def warm_up(model_cfg: dict) -> None:
    client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")
    try:
        client.chat.completions.create(
            model=model_cfg["ollama_model"],
            messages=[{"role": "user", "content": "reply with just: ok"}],
            extra_body=model_cfg.get("extra_body") or {},
        )
    except Exception:
        pass
