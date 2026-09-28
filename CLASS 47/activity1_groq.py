import config
from openai import OpenAI

GROQ_URL = "https://api.groq.com/openai/v1"

MODELS = getattr(
    config,
    "GROQ_MODELS",
    ["openai/gpt-oss-20b"]
)
def generate_response(
    prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 512
) -> str:
    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: GROQ_API_KEY missing in config.py"
    client = OpenAI(
        api_key=key,
        base_url=GROQ_URL
    )
    last_err = None

    for m in MODELS:
        try:
            response = client.chat.completions.create(
                model=m,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            last_err = e
    return f"Error: {last_err}"