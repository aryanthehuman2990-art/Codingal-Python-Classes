from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)
GROQ_MODELS = ["openai/gpt-oss-120b", "llama-3.3-70b-versatile"]

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 1024) -> str:
    last_err = None
    for model in GROQ_MODELS:
        try:
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return r.choices[0].message.content.strip()
        except Exception as e:
            last_err = e
    return f"⚠️ Groq request failed: {last_err}"