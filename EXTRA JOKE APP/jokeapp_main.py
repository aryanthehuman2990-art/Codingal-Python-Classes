"""
jokeapp_main.py - the app you run. Contains the interface, English jokes,
and the built-in Hinglish backup jokes.

Run:  streamlit run jokeapp_main.py
"""

import random

import requests
import streamlit as st

import config
import jokeapp_groq
import jokeapp_hf

# ---------------------------------------------------------------------------
# Backup jokes (used when the internet or an AI service is not available)
# ---------------------------------------------------------------------------

ENGLISH_BACKUP = [
    ("Why don't skeletons fight each other?", "They don't have the guts."),
    ("Why did the scarecrow win an award?", "He was outstanding in his field."),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs."),
    ("What do you call a fake noodle?", "An impasta."),
    ("Why did the math book look sad?", "It had too many problems."),
]

# Add your own Hinglish jokes here: (setup, punchline)
HINGLISH_JOKES = [
    ("Teacher: Pappu, batao sabse zyada barf kahan padti hai?",
     "Pappu: Sir, fridge mein."),
    ("Teacher: Ek saal mein kitne second hote hain?",
     "Pappu: 12 sir. 2 January, 2 February, 2 March..."),
    ("Mummy: Beta, padhai kar le, exam aa rahe hain.",
     "Pappu: Aane do mummy, main kaun sa unhe rokne wala hoon."),
    ("Interviewer: Aapki sabse badi kamzori kya hai?\n"
     "Candidate: Main bahut imaandaar hoon.\n"
     "Interviewer: Mujhe nahi lagta ye kamzori hai.",
     "Candidate: Mujhe aapki rai ki parwah bhi nahi hai."),
    ("Teacher: Agar tumhare paas 10 aam hain aur main 5 maang loon, toh kitne bachenge?",
     "Pappu: 10 hi sir. Main dunga hi nahi."),
    ("Golu: Doctor sahab, mujhe bhoolne ki bimari hai.\nDoctor: Kab se?",
     "Golu: Kab se kya?"),
    ("Patni: Suniye ji, aaj khana bahar khayenge.",
     "Pati: Theek hai, main chatai bahar bichha deta hoon."),
    ("Customer: Waiter, is soup mein makkhi hai!",
     "Waiter: Chinta mat kijiye sir, ye zyada nahi peeyegi."),
    ("Teacher: Zebra black and white kyun hota hai?",
     "Pappu: Sir, kyunki wo colour TV aane se pehle paida hua tha."),
    ("Papa: Itne kam number kyun aaye?\nPappu: Papa, wo absent tha na.\nPapa: Kaun?",
     "Pappu: Wo ladka jiski copy dekh ke main likhta hoon."),
    ("Golu ko neend nahi aa rahi thi. Dost bola: Bhed gin le.",
     "Golu: Gini yaar. 500 tak pahuncha toh subah ho gayi."),
    ("TT: Ye ticket toh bachche ka hai!",
     "Pappu: Toh dekh lijiye, aapki train ne kitna intezaar karwaya."),
    ("Teacher: Homework kyun nahi kiya?\nPappu: Sir, light chali gayi thi.\n"
     "Teacher: Toh mombatti jala lete.\nPappu: Maachis mandir mein thi.\n"
     "Teacher: Toh le aate.\nPappu: Nahaya nahi tha.\nTeacher: Kyun nahi nahaye?",
     "Pappu: Paani nahi tha sir, motor light se chalti hai."),
    ("Papa: Beta, Wi-Fi ka password kya hai?",
     "Beta: Pehle apna kamra saaf karo, phir milega."),
    ("Golu library mein: Bhaiya, ek burger aur fries dena.\nLibrarian: Ye library hai!",
     "Golu (dheere se): Sorry... ek burger aur fries dena."),
    ("Teacher: Pappu, tum class mein so kyun rahe ho?",
     "Pappu: Sir, aapki awaaz itni meethi hai, lori jaisi lagti hai."),
    ("Ek machhar ne doosre se poocha: Kal shaadi mein chalega?",
     "Doosra: Nahi yaar, wahan sab log taali bajate hain. Darr lagta hai."),
    ("Doctor: Aapko roz subah 5 km walk karni chahiye.\nMareez: Ji, ek mahine baad phone karunga.",
     "Doctor: Kyun? Mareez: Tab tak main 150 km door pahunch jaunga."),
    ("Teacher: Pappu, 'I don't know' ka matlab batao.\nPappu: Mujhe nahi pata sir.\n"
     "Teacher: Kal bhi yahi kaha tha, aaj bhi!",
     "Pappu: Toh sir, jawaab badlega thodi na?"),
    ("Biwi: Suno, main 5 minute mein tayyar hoke aati hoon.",
     "Pati: Theek hai, main tab tak naya ghar bana leta hoon."),
    ("Golu: Mummy, kal school nahi jaunga, sar dard ho raha hai.\nMummy: Kal toh Sunday hai.",
     "Golu: Dekha! Sar dard bhi time waste kar raha hai."),
    ("Bachcha: Papa, mobile mein charging kahan se aati hai?\nPapa: Bijli se.",
     "Bachcha: Toh phir bijli ka bill bhi mobile wale bharte honge na?"),
]

# ---------------------------------------------------------------------------
# Joke fetching
# ---------------------------------------------------------------------------

ENGINE_GROQ = "Groq AI"
ENGINE_HF = "Hugging Face AI"
ENGINE_BUILTIN = "Built-in jokes"


def fetch_english_joke(category: str) -> tuple[str, str, str]:
    """Return (setup, punchline, source). Tries two APIs, then the backup list."""
    try:
        r = requests.get(
            config.JOKEAPI_URL.format(category=category),
            params={"safe-mode": "", "type": "twopart"},
            timeout=config.REQUEST_TIMEOUT,
        )
        if r.status_code == 200:
            data = r.json()
            if not data.get("error"):
                return data["setup"], data["delivery"], "JokeAPI"
    except (requests.RequestException, ValueError, KeyError):
        pass

    try:
        r = requests.get(config.OFFICIAL_JOKE_URL, timeout=config.REQUEST_TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            return data["setup"], data["punchline"], "Official Joke API"
    except (requests.RequestException, ValueError, KeyError):
        pass

    setup, punch = random.choice(ENGLISH_BACKUP)
    return setup, punch, "offline backup"


def pick_builtin_hinglish() -> tuple[str, str, str]:
    """Random built-in joke, no repeats until the whole list has been shown."""
    pool = st.session_state.setdefault("hinglish_pool", [])
    if not pool:
        pool.extend(random.sample(range(len(HINGLISH_JOKES)), len(HINGLISH_JOKES)))
    setup, punch = HINGLISH_JOKES[pool.pop()]
    return setup, punch, "Built-in collection"


def fetch_hinglish_joke(engine: str) -> tuple[str, str, str]:
    """Ask the chosen AI; fall back to the built-in list and remember why."""
    st.session_state.ai_error = None
    recent = st.session_state.setdefault("recent_setups", [])
    providers = {ENGINE_GROQ: jokeapp_groq, ENGINE_HF: jokeapp_hf}

    if engine in providers:
        try:
            setup, punch = providers[engine].get_hinglish_joke(avoid=recent)
            recent.append(setup[:80])
            return setup, punch, engine
        except RuntimeError as exc:
            st.session_state.ai_error = str(exc)

    return pick_builtin_hinglish()


def available_engines() -> list[str]:
    engines = []
    if jokeapp_groq.is_available():
        engines.append(ENGINE_GROQ)
    if jokeapp_hf.is_available():
        engines.append(ENGINE_HF)
    engines.append(ENGINE_BUILTIN)
    return engines


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Hasi Mazaak", page_icon="😂", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;800&family=Nunito:wght@400;600&display=swap');

    :root {
        --ink: #2b1a3d;
        --marigold: #f7a928;
        --rani: #e0367a;
        --paper: #fff8ec;
        --muted: #7a6a86;
    }
    .stApp { background: radial-gradient(circle at 15% 0%, #ffe3b0 0%, var(--paper) 45%); }
    html, body, [class*="css"], .stMarkdown, p, label { font-family: 'Nunito', sans-serif; color: var(--ink); }

    .brand { font-family: 'Baloo 2', cursive; font-weight: 800; font-size: 3.2rem;
             line-height: 1; margin: 0; color: var(--ink); }
    .brand span { color: var(--rani); }
    .tagline { color: var(--muted); margin: .3rem 0 1.4rem; font-size: 1.05rem; }

    .joke-card { background: #fff; border-radius: 22px; padding: 1.8rem 1.8rem 1.4rem;
                 border: 3px solid var(--ink); box-shadow: 8px 8px 0 var(--marigold);
                 margin: 1rem 0 1.2rem; }
    .setup { font-family: 'Baloo 2', cursive; font-weight: 600; font-size: 1.45rem;
             line-height: 1.35; white-space: pre-line; margin: 0; color: var(--ink); }
    .punch { font-family: 'Baloo 2', cursive; font-weight: 800; font-size: 1.5rem;
             color: var(--rani); white-space: pre-line; margin: 1rem 0 0;
             animation: pop .35s ease-out; }
    .waiting { color: var(--muted); font-style: italic; margin: 1rem 0 0; }
    .source { font-size: .8rem; color: var(--muted); margin-top: 1rem;
              text-transform: uppercase; letter-spacing: .08em; }
    .empty { text-align: center; padding: 2.2rem 1rem; color: var(--muted); }
    .empty b { font-family: 'Baloo 2', cursive; font-size: 1.4rem; color: var(--ink); }
    @keyframes pop { from { transform: scale(.9); opacity: 0; } to { transform: scale(1); opacity: 1; } }
    @media (prefers-reduced-motion: reduce) { .punch { animation: none; } }

    div.stButton > button { border-radius: 999px; border: 2px solid var(--ink);
        font-family: 'Baloo 2', cursive; font-weight: 600; font-size: 1.05rem;
        padding: .45rem 1.3rem; }
    div.stButton > button[kind="primary"] { background: var(--ink); color: #fff; }
    div.stButton > button[kind="primary"]:hover { background: var(--rani); border-color: var(--rani); }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="brand">Hasi <span>Mazaak</span></p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Ek joke, do bhashayein. One tap, one laugh.</p>',
            unsafe_allow_html=True)

st.session_state.setdefault("joke", None)
st.session_state.setdefault("revealed", False)
st.session_state.setdefault("count", 0)

col_lang, col_opt = st.columns(2)
with col_lang:
    language = st.radio("Language", ["English", "Hinglish"], horizontal=True, key="language")
with col_opt:
    if language == "English":
        cat_label = st.selectbox("Type of joke", list(config.ENGLISH_CATEGORIES), key="category")
    else:
        engine = st.selectbox("Joke source", available_engines(), key="engine")

b1, b2, _ = st.columns([1.4, 1.4, 1])
with b1:
    if st.button("Tell me a joke", type="primary", use_container_width=True, key="new_joke"):
        with st.spinner("Joke soch raha hoon..."):
            if language == "English":
                st.session_state.ai_error = None
                joke = fetch_english_joke(config.ENGLISH_CATEGORIES[cat_label])
            else:
                joke = fetch_hinglish_joke(engine)
        st.session_state.joke = joke
        st.session_state.revealed = False
        st.session_state.count += 1
with b2:
    reveal_label = "Punchline batao!" if language == "Hinglish" else "Show punchline"
    if st.button(reveal_label, use_container_width=True, key="reveal",
                 disabled=st.session_state.joke is None or st.session_state.revealed):
        st.session_state.revealed = True
        st.rerun()

joke = st.session_state.joke
if joke:
    setup, punch, source = joke
    punch_html = (
        f'<p class="punch">{punch}</p>' if st.session_state.revealed
        else '<p class="waiting">Socho, socho...</p>'
    )
    st.markdown(
        f'<div class="joke-card"><p class="setup">{setup}</p>{punch_html}'
        f'<div class="source">Joke #{st.session_state.count} · {source}</div></div>',
        unsafe_allow_html=True,
    )
    if st.session_state.get("ai_error"):
        st.caption(f"{st.session_state.ai_error.rstrip('.')}. Showing a built-in joke instead.")
else:
    st.markdown(
        '<div class="joke-card empty"><b>Ready when you are.</b><br>'
        'Pick a language and hit “Tell me a joke”.</div>',
        unsafe_allow_html=True,
    )

if language == "Hinglish" and len(available_engines()) == 1:
    st.caption("Add GROQ_API_KEY or HF_TOKEN to your .env file to get AI-written Hinglish jokes.")