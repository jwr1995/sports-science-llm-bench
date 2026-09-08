# sports-science-llm-bench

A small benchmark for evaluating whether a local LLM (served via
[Ollama](https://ollama.com)) actually has postgraduate-level knowledge of
exercise physiology, training theory, and sports data science methodology —
the kind of understanding you'd expect from someone who'd pass an MSc in
Data Science and Sports Science with flying colours.

## Why this exists

If you're picking a local model to power a coaching-dashboard agent, tool-
calling reliability is necessary but not sufficient: the model also has to
reason correctly about the domain once the tools have handed back data. This
repo tests that second half in isolation — pure knowledge and applied
critical thinking, no tools, single-turn questions with rubric-based
grading.

It's a companion to, but fully independent of, a private repo
(`coachllm`) that benchmarks tool-calling against one athlete's personal
training data. This repo is deliberately self-contained — no dependency on
that repo or any private data — so it's safe to publish on GitHub.

## Setup

Requires [Ollama](https://ollama.com) running locally with your candidate
models pulled, and [`uv`](https://docs.astral.sh/uv/) installed.

```bash
uv sync
uv run python run_exam.py
```

Edit `models.py` to match whatever models you've actually pulled — nothing
else needs to change. See its docstring for how the `extra_body` field maps
to reasoning-effort / thinking-mode toggles, which vary by model.

Useful flags:

```bash
uv run python run_exam.py --models qwen3-30b-a3b        # one model, both context conditions
uv run python run_exam.py --context with                 # only the with-context condition
uv run python run_exam.py --questions critical_power_model,minetti_descent
```

Results are written as JSON to `results/<timestamp>/`, one file per
model/context combination, plus a summary table printed to stdout.

## How grading works (and its honest limitation)

`grading.py` does lenient, case-insensitive keyword/phrase matching: each
question in `questions.py` has a `key_points` rubric (concept groups, each
satisfied by any one of several phrasings) and a `red_flags` list (phrases
indicating a common misconception). Coverage is the fraction of key points
matched; red flags are reported separately.

This is a coarse proxy, not a semantic grader. It's good for ranking
candidates and for triaging which transcripts are worth reading closely —
it is **not** a substitute for actually reading the answers in
`results/*.json`, especially for the `critical_thinking` category, where a
model can use all the right words while still reasoning about them
incorrectly (or vice versa: give a correct answer in unexpected phrasing
that the keyword match misses).

## What the "with-context" condition tests

`context.md` is a curated sheet of canonical, well-established sports-
science and sports-data-science reference material (critical power theory,
Minetti's cost-of-locomotion curve, Banister's impulse-response model,
ACWR critique, polarized training, out-of-sample validation, etc). When
`run_exam.py` runs the "with-context" condition, this file is prepended to
the system prompt.

Comparing with-context vs without-context coverage and red-flag counts
answers a genuinely useful product question: does grounding the model in a
good reference document measurably improve its answers, or reduce
fabricated/wrong claims? If it does, that's a strong argument for shipping
a similar reference document in the coaching-dashboard agent's own system
prompt.

## Adding a question or a model

- **Models**: add an entry to the `CANDIDATES` list in `models.py` — see
  its docstring for the shape of each entry.
- **Questions**: add an entry to the `QUESTIONS` list in `questions.py`,
  following the existing structure — `id`, `category`, `prompt`,
  `key_points` (list of `{desc, any_of}`), and `red_flags` (same shape).
  Keep `any_of` phrases lenient and lowercase-matchable; grading does plain
  substring matching, not stemming or synonym expansion.

## License

MIT — see `LICENSE`. This benchmark is meant to be forkable: swap
`questions.py` and `context.md` for a different subject's rubric and
reference material, and the runner/grader infrastructure carries over
unchanged.
