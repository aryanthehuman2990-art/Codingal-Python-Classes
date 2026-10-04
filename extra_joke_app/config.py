"""
config.py - settings shared by the joke app.

Keys are read from (first one found wins):
  1. Streamlit Cloud secrets  (Manage app -> Settings -> Secrets)
  2. a local .env file        (GROQ_API_KEY=..., HF_TOKEN=...)
"""

import json
import os
import re

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _secret(name: str) -> str:
    try:
        import streamlit as st
        if name in st.secrets:
            return str(st.secrets[name]).strip()
    except Exception:  # no secrets file locally -> fall back to .env
        pass
    return os.getenv(name, "").strip()


# ---------------------------------------------------------------------------
# Joke websites (English)
# ---------------------------------------------------------------------------
JOKEAPI_URL = "https://v2.jokeapi.dev/joke/{category}"
OFFICIAL_JOKE_URL = "https://official-joke-api.appspot.com/random_joke"
REQUEST_TIMEOUT = 8  # seconds

# ---------------------------------------------------------------------------
# AI providers
# ---------------------------------------------------------------------------
GROQ_API_KEY = _secret("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = _secret("GROQ_MODEL") or "llama-3.3-70b-versatile"

HF_TOKEN = _secret("HF_TOKEN")
HF_URL = "https://router.huggingface.co/v1/chat/completions"
HF_MODEL = _secret("HF_MODEL") or "meta-llama/Llama-3.3-70B-Instruct"

AI_TIMEOUT = 25        # seconds
AI_TEMPERATURE = 1.0   # higher = more variety

# ---------------------------------------------------------------------------
# Prompt (used by both AI providers)
# ---------------------------------------------------------------------------
LANGUAGE_RULES = {
    "English": "Write in simple, natural English.",
    "Hinglish": ("Write in Hinglish: Hindi written in Roman (English) letters, mixed with "
                 "everyday English words, the way people text in India. No Devanagari script."),
}


def build_messages(language: str, style: str | None, avoid: list[str]) -> list[dict]:
    style_line = f"Joke type: {style}." if style else "Joke type: any type you like."
    avoid_line = ""
    if avoid:
        avoid_line = "Do NOT repeat or rework these recent jokes:\n- " + "\n- ".join(avoid[-10:])
    system = (
        "You are a witty, family-friendly comedian. Jokes must be clean and suitable for all ages: "
        "no insults about religion, caste, gender, body or any community, no politics, no adult content. "
        'Reply ONLY with JSON: {"setup": "...", "punchline": "..."}. '
        "The setup builds up the joke; the punchline is the payoff, kept short. "
        "Use \\n for line breaks in dialogue."
    )
    user = f"{LANGUAGE_RULES.get(language, LANGUAGE_RULES['English'])}\n{style_line}\n{avoid_line}".strip()
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def parse_joke(text: str) -> tuple[str, str]:
    """Pull (setup, punchline) out of the model's reply. Raises RuntimeError if it can't."""
    match = re.search(r"\{.*\}", text or "", re.DOTALL)
    if not match:
        raise RuntimeError("The AI reply wasn't in the expected format")
    try:
        data = json.loads(match.group(0))
        setup, punch = str(data["setup"]).strip(), str(data["punchline"]).strip()
    except (ValueError, KeyError, TypeError):
        raise RuntimeError("The AI reply wasn't in the expected format")
    if not setup or not punch:
        raise RuntimeError("The AI sent an empty joke")
    return setup, punch