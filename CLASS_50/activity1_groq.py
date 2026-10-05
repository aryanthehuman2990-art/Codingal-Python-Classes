import os
from openai import OpenAI

# config.py is only on your computer (not on GitHub)
try:
    import config
except ImportError:
    config = None

GROQ_URL = "https://api.groq.com/openai/v1"

MODELS = getattr(config, "GROQ_MODELS", ["openai/gpt-oss-20b"])


def get_api_key():
    # On Streamlit Cloud: comes from Secrets
    # On your computer: comes from config.py
    return os.getenv("GROQ_API_KEY") or getattr(config, "GROQ_API_KEY", None)


def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = get_api_key()
    if not key:
        return "Error: GROQ_API_KEY is missing. Add it in Streamlit Secrets."

    client = OpenAI(api_key=key, base_url=GROQ_URL)
    last_err = None

    for m in MODELS:
        try:
            response = client.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            last_err = e

    return f"Error: {last_err}"