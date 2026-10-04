"""
jokeapp_hf.py - gets a Hinglish joke from a Hugging Face model.

Test this file on its own:  python jokeapp_hf.py
"""

from huggingface_hub import InferenceClient

import config


def is_available() -> bool:
    return bool(config.HF_TOKEN)


def get_hinglish_joke(avoid: list[str] | None = None) -> tuple[str, str]:
    """Return (setup, punchline). Raises RuntimeError with a readable reason on failure."""
    if not is_available():
        raise RuntimeError("HF_TOKEN is missing from .env")

    client = InferenceClient(api_key=config.HF_TOKEN, timeout=config.REQUEST_TIMEOUT)
    try:
        response = client.chat_completion(
            model=config.HF_MODEL,
            messages=[
                {"role": "system", "content": config.SYSTEM_PROMPT},
                {"role": "user", "content": config.build_hinglish_prompt(avoid)},
            ],
            temperature=0.9,
            max_tokens=300,
        )
    except Exception as exc:
        raise RuntimeError(f"Hugging Face request failed: {exc}") from exc

    joke = config.parse_joke(response.choices[0].message.content or "")
    if not joke:
        raise RuntimeError("Hugging Face replied, but not in the expected joke format")
    return joke


if __name__ == "__main__":
    setup, punchline = get_hinglish_joke()
    print(setup)
    print("->", punchline)