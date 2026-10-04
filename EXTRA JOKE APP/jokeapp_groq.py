"""
jokeapp_groq.py - gets a Hinglish joke from Groq.

Test this file on its own:  python jokeapp_groq.py
"""

from groq import Groq

import config


def is_available() -> bool:
    return bool(config.GROQ_API_KEY)


def get_hinglish_joke(avoid: list[str] | None = None) -> tuple[str, str]:
    """Return (setup, punchline). Raises RuntimeError with a readable reason on failure."""
    if not is_available():
        raise RuntimeError("GROQ_API_KEY is missing from .env")

    client = Groq(api_key=config.GROQ_API_KEY, timeout=config.REQUEST_TIMEOUT)
    try:
        response = client.chat.completions.create(
            model=config.GROQ_MODEL,
            messages=[
                {"role": "system", "content": config.SYSTEM_PROMPT},
                {"role": "user", "content": config.build_hinglish_prompt(avoid)},
            ],
            temperature=1.0,
            max_tokens=300,
            response_format={"type": "json_object"},
        )
    except Exception as exc:
        raise RuntimeError(f"Groq request failed: {exc}") from exc

    joke = config.parse_joke(response.choices[0].message.content or "")
    if not joke:
        raise RuntimeError("Groq replied, but not in the expected joke format")
    return joke


if __name__ == "__main__":
    setup, punchline = get_hinglish_joke()
    print(setup)
    print("->", punchline)