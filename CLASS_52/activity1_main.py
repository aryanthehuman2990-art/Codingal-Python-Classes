import io
import html
from io import BytesIO

from urllib.parse import quote

import requests
import streamlit as st
from PIL import Image

from activity1_groq import generate_response


MATH_SYSTEM = """You are a Math Mastermind.
Solve with clear step-by-step reasoning, correct notation, and a final answer.
Verify when possible; mention an alternative method briefly if relevant."""

CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.card{border:1px solid #e6e6e6;background:#fff;border-radius:10px;padding:14px 16px;margin:10px 0;
box-shadow:0 1px 2px rgba(0,0,0,0.04);}
.q{font-weight:700;color:#0a6ebd;margin-bottom:8px;}
.meta{display:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radius:12px;font-size:12px;margin-left:8px}
.a{white-space:pre-wrap;color:#333;line-height:1.5;}
</style>
"""


def esc(text) -> str:
    """Escape user/model text so characters like < > & don't break the HTML cards."""
    return html.escape(str(text))


def export_txt(history):
    txt = "".join(
        f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n"
        for i, h in enumerate(history, 1)
    )
    bio = io.BytesIO(txt.encode("utf-8"))
    bio.seek(0)
    return bio


def teaching_answer(q: str) -> str:
    return generate_response(q, temperature=0.3, max_tokens=1024)


def math_answer(q: str, level: str) -> str:
    prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\nMath Problem: {q}"
    return generate_response(prompt, temperature=0.1, max_tokens=1024)


# ---------------- AI Teaching Assistant ----------------
def run_ai_teaching_assistant():
    st.title("🤖 AI Teaching Assistant")
    st.session_state.setdefault("history_ata", [])

    c1, c2 = st.columns([1, 2])
    if c1.button("🧹 Clear", key="c_ata"):
        st.session_state.history_ata = []
        st.rerun()
    if st.session_state.history_ata:
        c2.download_button(
            "📄 Export",
            export_txt(st.session_state.history_ata),
            "AI_Teaching_Assistant_Conversation.txt",
            "text/plain",
        )

    q = st.text_input("Enter your question:", key="q_ata")
    if st.button("Ask", key="a_ata"):
        if not q.strip():
            st.warning("⚠️ Enter a question.")
        else:
            with st.spinner("Thinking..."):
                ans = teaching_answer(q.strip())
            st.session_state.history_ata.append({"question": q.strip(), "answer": ans})
            st.rerun()

    if not st.session_state.history_ata:
        return

    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    out = '<div class="wrap">'
    for i, qa in enumerate(st.session_state.history_ata, 1):
        out += (
            f'<div class="card"><div class="q">Q{i}: {esc(qa["question"])}</div>'
            f'<div class="a">{esc(qa["answer"])}</div></div>'
        )
    st.markdown(out + "</div>", unsafe_allow_html=True)


# ---------------- Math Mastermind ----------------
def run_math_mastermind():
    st.title("🧮 Math Mastermind")
    st.session_state.setdefault("history_mm", [])

    c1, c2 = st.columns([1, 2])
    if c1.button("🧹 Clear", key="c_mm"):
        st.session_state.history_mm = []
        st.rerun()
    if st.session_state.history_mm:
        c2.download_button(
            "📄 Export",
            export_txt(st.session_state.history_mm),
            "Math_Mastermind_Solutions.txt",
            "text/plain",
        )

    with st.form("mm_form", clear_on_submit=True):
        q = st.text_area("Math problem:", height=100)
        a, b = st.columns([3, 1])
        lvl = b.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)
        go = a.form_submit_button("Solve", use_container_width=True)

    if go:
        if not q.strip():
            st.warning("⚠️ Enter a problem.")
        else:
            with st.spinner("Solving..."):
                ans = math_answer(q.strip(), lvl)
            st.session_state.history_mm.insert(
                0, {"question": q.strip(), "answer": ans, "difficulty": lvl}
            )
            st.rerun()

    if not st.session_state.history_mm:
        return

    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    out = '<div class="wrap">'
    for i, qa in enumerate(st.session_state.history_mm, 1):
        out += (
            f'<div class="card"><div class="q">Q{i}: {esc(qa["question"])}'
            f'<span class="meta">{esc(qa["difficulty"])}</span></div>'
            f'<div class="a">{esc(qa["answer"])}</div></div>'
        )
    st.markdown(out + "</div>", unsafe_allow_html=True)


# ---------------- Safe AI Image Generator ----------------
FILTER_API_URL = "https://filters-zeta.vercel.app/api/filter"
# Free image API, no key needed. Model options: "flux", "turbo"
IMG_API_URL = "https://image.pollinations.ai/prompt/{prompt}"
IMG_MODEL = "flux"


def is_prompt_safe(prompt: str):
    try:
        response = requests.post(FILTER_API_URL, json={"text": prompt}, timeout=15)
        if response.status_code != 200:
            return False, f"Filter API failed with status {response.status_code}: {response.text}"
        data = response.json()
        if data.get("ok") is True:
            return True, None
        return False, data.get("reason", "⚠️ Unsafe prompt.")
    except Exception as e:
        return False, f"Filter API error: {e}"


def generate_image(prompt: str):
    safe, err = is_prompt_safe(prompt)
    if not safe:
        return None, err
    try:
        url = IMG_API_URL.format(prompt=quote(prompt))
        params = {"width": 1024, "height": 1024, "model": IMG_MODEL, "nologo": "true"}
        r = requests.get(url, params=params, timeout=90)
        if r.status_code != 200:
            return None, f"Image API failed with status {r.status_code}: {r.text[:200]}"
        image = Image.open(BytesIO(r.content)).convert("RGB")
        return image, None
    except Exception as e:
        return None, f"Error during image generation: {e}"


def run_safe_ai_image_generator():
    st.title("🖼️ Safe AI Image Generator")

    with st.form("img_form"):
        p = st.text_area("Image description:", height=120)
        ok = st.form_submit_button("Generate Image")

    if ok:
        if not p.strip():
            st.warning("⚠️ Enter a description.")
        else:
            with st.spinner("Generating image..."):
                im, err = generate_image(p.strip())
            if err:
                st.error(err)
                st.session_state.pop("generated_image", None)
            else:
                st.session_state.generated_image = im

    im = st.session_state.get("generated_image")
    if im is not None:
        st.image(im, use_container_width=True)
        buf = BytesIO()
        im.save(buf, format="PNG")
        st.download_button(
            "📥 Download", buf.getvalue(), "ai_generated_image.png", "image/png"
        )


# ---------------- Main ----------------
def main():
    st.sidebar.title("Choose AI Feature")
    opt = st.sidebar.selectbox(
        "Feature",
        ["AI Teaching Assistant", "Math Mastermind", "Safe AI Image Generator"],
        label_visibility="collapsed",
    )
    if opt == "AI Teaching Assistant":
        run_ai_teaching_assistant()
    elif opt == "Math Mastermind":
        run_math_mastermind()
    else:
        run_safe_ai_image_generator()


if __name__ == "__main__":
    main()