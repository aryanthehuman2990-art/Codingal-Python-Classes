"""
config.py - settings shared by every file in the app.

Keys are read from the .env file (locally) or from environment variables /
Space secrets (on Hugging Face). Nothing secret is written in this file.
"""

import json
import os
import random
import re

from dotenv import load_dotenv

load_dotenv()  # reads .env if it exists; does nothing on Hugging Face

# --- API keys --------------------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
HF_TOKEN = os.getenv("HF_TOKEN", "").strip()

# --- Models (change in .env if one stops working) --------------------------
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
HF_MODEL = os.getenv("HF_MODEL", "Qwen/Qwen2.5-7B-Instruct")

# --- English joke APIs -----------------------------------------------------
JOKEAPI_URL = "https://v2.jokeapi.dev/joke/{category}"
OFFICIAL_JOKE_URL = "https://official-joke-api.appspot.com/random_joke"

ENGLISH_CATEGORIES = {
    "Anything": "Any",
    "Programming": "Programming",
    "Puns": "Pun",
    "Misc": "Misc",
    "Spooky": "Spooky",
    "Christmas": "Christmas",
}

REQUEST_TIMEOUT = 15  # seconds

# --- Shared AI prompt ------------------------------------------------------
JOKE_THEMES = [
    "school and teachers", "parents and kids", "doctor visits", "office life",
    "Indian weddings", "cricket", "trains and travel", "mobile phones and Wi-Fi",
    "food and restaurants", "neighbours", "exams and results", "shopkeepers",
    "monsoon and weather", "traffic", "grandparents", "pets",
]

SYSTEM_PROMPT = "You are a witty Indian stand-up comic who writes clean, family-friendly jokes."


def build_hinglish_prompt(avoid: list[str] | None = None) -> str:
    """The instruction both Groq and Hugging Face receive."""
    theme = random.choice(JOKE_THEMES)
    prompt = (
        f"Write one short, original, funny Hindi joke about {theme}. "
        "Write it in Hinglish: Hindi words in Roman (English) letters, for example "
        "'Teacher: Pappu, batao sabse zyada barf kahan padti hai?'. "
        "Never use Devanagari script. Keep it clean, with no jokes about religion, "
        "caste, community, gender stereotypes or body shaming. "
        "If it is a dialogue, put each speaker on a new line as 'Name: line'. "
        'Reply with JSON only, in this exact shape: {"setup": "...", "punchline": "..."}'
    )
    if avoid:
        prompt += "\nDo not repeat any of these: " + " | ".join(avoid[-5:])
    return prompt


def parse_joke(text: str) -> tuple[str, str] | None:
    """Pull {"setup", "punchline"} out of a model reply, even if it added extra text."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
        setup = str(data.get("setup", "")).strip()
        punch = str(data.get("punchline", "")).strip()
    except (ValueError, AttributeError):
        return None
    if not setup or not punch:
        return None
    return setup, punch