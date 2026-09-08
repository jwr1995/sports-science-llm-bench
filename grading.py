"""Rubric-based heuristic grading for exam answers.

This is NOT a full NLP/semantic grader — it's deliberately simple and
transparent: does the answer's text contain (a lenient case-insensitive
substring match on) at least one phrase from each key_point's `any_of`
list, and does it avoid any red_flag phrase. That's a coarse proxy for
concept coverage, good enough to rank candidates and to point you at
which transcripts are worth reading — it is not a substitute for actually
reading the answers, especially for the critical_thinking category where
nuance matters more than keyword coverage.
"""
from __future__ import annotations


def grade(question: dict, answer: str) -> dict:
    text = (answer or "").lower()

    hits = []
    for kp in question["key_points"]:
        hit = any(phrase.lower() in text for phrase in kp["any_of"])
        hits.append({"desc": kp["desc"], "hit": hit})

    flags = []
    for rf in question.get("red_flags", []):
        triggered = any(phrase.lower() in text for phrase in rf["any_of"])
        if triggered:
            flags.append(rf["desc"])

    n_hit = sum(1 for h in hits if h["hit"])
    coverage = n_hit / len(hits) if hits else 0.0

    return {
        "coverage": round(coverage, 2),
        "key_points_hit": hits,
        "red_flags_triggered": flags,
    }
