"""
jokeapp_hf.py - jokes written by a Hugging Face model.

Needs HF_TOKEN (free token: https://huggingface.co/settings/tokens,
tick "Make calls to Inference Providers" when creating it).
Any problem is raised as RuntimeError so the app can fall back to built-in jokes.
"""

import requests

import config


def is_available() -> bool:
    return bool(config.HF_TOKEN)


def get_joke(language: str = "Hinglish", style: str | None = None,
             avoid: list[str] | None = None) -> tuple[str, str]:
    if not is_available():
        raise RuntimeError("Hugging Face token not set")
    try:
        r = requests.post(
            config.HF_URL,
            headers={"Authorization": f"Bearer {config.HF_TOKEN}"},
            json={
                "model": config.HF_MODEL,
                "messages": config.build_messages(language, style, avoid or []),
                "temperature": config.AI_TEMPERATURE,
                "max_tokens": 300,
            },
            timeout=config.AI_TIMEOUT,
        )
    except requests.RequestException:
        raise RuntimeError("Couldn't reach Hugging Face")

    if r.status_code in (401, 403):
        raise RuntimeError("Hugging Face rejected the token")
    if r.status_code == 402:
        raise RuntimeError("Hugging Face free credits are used up for this month")
    if r.status_code == 429:
        raise RuntimeError("Hugging Face is busy (rate limit), try again in a minute")
    if r.status_code != 200:
        raise RuntimeError(f"Hugging Face error {r.status_code}")

    try:
        text = r.json()["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError):
        raise RuntimeError("Hugging Face sent an unexpected reply")
    return config.parse_joke(text)


def get_hinglish_joke(avoid: list[str] | None = None, style: str | None = None) -> tuple[str, str]:
    """Kept for older code that calls this name."""
    return get_joke("Hinglish", style, avoid)