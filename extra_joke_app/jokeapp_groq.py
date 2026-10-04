"""
jokeapp_groq.py - jokes written by Groq AI.

Needs GROQ_API_KEY (free key: https://console.groq.com/keys).
Any problem is raised as RuntimeError so the app can fall back to built-in jokes.
"""

import requests

import config


def is_available() -> bool:
    return bool(config.GROQ_API_KEY)


def get_joke(language: str = "Hinglish", style: str | None = None,
             avoid: list[str] | None = None) -> tuple[str, str]:
    if not is_available():
        raise RuntimeError("Groq key not set")
    try:
        r = requests.post(
            config.GROQ_URL,
            headers={"Authorization": f"Bearer {config.GROQ_API_KEY}"},
            json={
                "model": config.GROQ_MODEL,
                "messages": config.build_messages(language, style, avoid or []),
                "temperature": config.AI_TEMPERATURE,
                "max_tokens": 300,
                "response_format": {"type": "json_object"},
            },
            timeout=config.AI_TIMEOUT,
        )
    except requests.RequestException:
        raise RuntimeError("Couldn't reach Groq")

    if r.status_code == 401:
        raise RuntimeError("Groq rejected the API key")
    if r.status_code == 429:
        raise RuntimeError("Groq is busy (rate limit), try again in a minute")
    if r.status_code != 200:
        raise RuntimeError(f"Groq error {r.status_code}")

    try:
        text = r.json()["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError):
        raise RuntimeError("Groq sent an unexpected reply")
    return config.parse_joke(text)


def get_hinglish_joke(avoid: list[str] | None = None, style: str | None = None) -> tuple[str, str]:
    """Kept for older code that calls this name."""
    return get_joke("Hinglish", style, avoid)
