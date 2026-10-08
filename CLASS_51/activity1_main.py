from activity1_groq import generate_response
import io
import re
import streamlit as st


SYSTEM_PROMPT = """You are a Math Mastermind. For every math problem:
1) Show step-by-step solution  2) Explain reasoning  3) Give alternate method if possible
4) Verify answer if possible  5) Use proper notation  6) Break complex problems into parts
Format: Problem → Steps → **Final Answer** → Concepts used. Be precise and educational.
Math formatting rules (output is rendered by Streamlit Markdown):
- Inline math: $...$   - Display math: $$...$$ on its own line
- Never use \\[ \\] or \\( \\) as math delimiters"""


def math_generate(problem: str, level: str, temperature=0.1, max_tokens=1024) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nMath Problem ({level}): {problem}"
    return generate_response(prompt, temperature=temperature, max_tokens=max_tokens)


def to_streamlit_latex(text: str) -> str:
    """Convert LaTeX the model may still emit into delimiters Streamlit renders."""
    text = re.sub(r"\\\[(.+?)\\\]", lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n", text, flags=re.S)
    text = re.sub(r"\\\((.+?)\\\)", lambda m: f"${m.group(1).strip()}$", text, flags=re.S)
    return text


def export_txt(history):
    txt = "\n\n".join(
        f"Q{i} [{h['lvl']}]: {h['q']}\nA{i}: {h['a']}" for i, h in enumerate(history, 1)
    )
    return io.BytesIO(txt.encode("utf-8"))


def setup_ui():
    st.set_page_config(page_title="🧮 Math Mastermind", layout="centered")
    st.title("🧮 Math Mastermind")
    st.write("Solve any math problem with detailed step-by-step explanations.")

    with st.expander("📌 Examples"):
        st.markdown(
            '- Algebra: "Solve 2x² + 5x − 3 = 0"\n'
            '- Calculus: "Derivative of sin(x²) + ln(x)"\n'
            '- Geometry: "Area of triangle (0,0),(3,4),(6,0)"\n'
            '- Probability: "P(sum=7 with two dice)"'
        )

    st.session_state.setdefault("history", [])

    c1, c2 = st.columns([1, 2])
    if c1.button("🗑️ Clear"):
        st.session_state.history = []
        st.rerun()

    if st.session_state.history:
        c2.download_button("📄 Export", export_txt(st.session_state.history),
                           "Math_Mastermind_Solutions.txt", "text/plain")

    with st.form("math_form", clear_on_submit=True):
        q = st.text_area("📝 Enter your math problem:", height=100,
                         placeholder="Example: Solve x² + 5x + 6 = 0")
        a, b = st.columns([3, 1])
        solve = a.form_submit_button("🧠 Solve", use_container_width=True)
        level = b.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)

    if solve:
        if not q.strip():
            st.warning("⚠️ Enter a problem first.")
        else:
            with st.spinner("Solving..."):
                ans = math_generate(q.strip(), level)
            st.session_state.history.insert(0, {"q": q.strip(), "a": ans, "lvl": level})
            st.rerun()

    if not st.session_state.history:
        return

    st.markdown("### 🧾 Solution History (Latest First)")
    with st.container(height=500, border=True):   # scrollable box, needs Streamlit >= 1.32
        for i, h in enumerate(st.session_state.history, 1):
            st.markdown(f"**Q{i}:** {h['q']} &nbsp; :orange-background[{h['lvl']}]")
            with st.container(border=True):
                st.markdown(to_streamlit_latex(h["a"]))


if __name__ == "__main__":
    setup_ui()