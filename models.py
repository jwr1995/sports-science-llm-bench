"""Candidate local models to benchmark, served via Ollama.

`ollama_model` must already be pulled (`ollama pull <name>`). `extra_body`
is merged into the OpenAI-compatible chat request as-is — this is where a
reasoning-effort / thinking-mode toggle goes for models that support one.
The exact field name and valid values vary by model and by Ollama version
(commonly `reasoning_effort`: "none"/"low"/"medium"/"high", but check
`ollama show <model> --modelfile` and that model's own docs before trusting
this blindly).

Edit this list to match whatever you've pulled locally — nothing else in
this repo needs to change.
"""

CANDIDATES = [
    {
        "name": "qwen3.8-27b-low-reasoning",
        "ollama_model": "qwen3.8:27b",
        "extra_body": {"reasoning_effort": "low"},
    },
    {
        "name": "qwen3.8-27b-high-reasoning",
        "ollama_model": "qwen3.8:27b",
        "extra_body": {"reasoning_effort": "high"},
    },
    {
        "name": "qwen3-30b-a3b",
        "ollama_model": "qwen3:30b-a3b-instruct-2507-q4_K_M",
        "extra_body": {},
    },
    {
        "name": "gpt-oss-20b",
        "ollama_model": "gpt-oss:20b",
        "extra_body": {"reasoning_effort": "medium"},
    },
]
