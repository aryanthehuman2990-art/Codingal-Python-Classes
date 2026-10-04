"""
jokeapp_main.py - Hasi Mazaak: the app you run.

Flow:  1) pick a language (English / Hinglish)
       2) pick a joke type (Random, One-liner, Wordplay, Observational,
          Anecdotal, Situational)
       3) get a joke, reveal the punchline, rate it, save favourites.

Joke sources (tried in order, falls back automatically):
  - Public joke APIs (English Random / Wordplay only)
  - Groq / Hugging Face AI (if keys are in .env)
  - Built-in collection below (always works, even offline)

Look and feel: CSS only (no HTML) - see the Styles section.

Run:  streamlit run jokeapp_main.py
"""

import inspect
import random

import requests
import streamlit as st

import config
import jokeapp_groq
import jokeapp_hf

# ---------------------------------------------------------------------------
# Joke types
# ---------------------------------------------------------------------------

RANDOM = "Random"
JOKE_TYPES = {
    "One-liner": ("⚡", "Short and punchy. Setup and punchline land almost together."),
    "Wordplay": ("🔤", "Puns, double meanings and clever twists on words."),
    "Observational": ("🔍", "Everyday life quirks. Funny because it's true."),
    "Anecdotal": ("📖", "A little story that builds up to the payoff."),
    "Situational": ("🎭", "Characters in a funny setup: teacher, doctor, boss, waiter..."),
}
TYPE_ICONS = {RANDOM: "🎲", "Surprise": "🎲", "Mixed": "🎲", **{k: v[0] for k, v in JOKE_TYPES.items()}}

# ---------------------------------------------------------------------------
# Built-in jokes: JOKES[language][type] = [(setup, punchline), ...]
# Add your own anywhere - they'll show up automatically.
# ---------------------------------------------------------------------------

JOKES = {
    "English": {
        "One-liner": [
            ("I told my wife she was drawing her eyebrows too high.", "She looked surprised."),
            ("I'm reading a book about anti-gravity.", "It's impossible to put down."),
            ("I used to play piano by ear.", "Now I use my hands."),
            ("I have a fear of speed bumps.", "But I'm slowly getting over it."),
            ("I asked the librarian if they had books on procrastination.",
             "She said she'd get back to me."),
        ],
        "Wordplay": [
            ("Why don't skeletons fight each other?", "They don't have the guts."),
            ("Why did the scarecrow win an award?", "He was outstanding in his field."),
            ("Why do programmers prefer dark mode?", "Because light attracts bugs."),
            ("What do you call a fake noodle?", "An impasta."),
            ("Why did the math book look sad?", "It had too many problems."),
            ("Why can't a bicycle stand up on its own?", "It's two tired."),
        ],
        "Observational": [
            ("We spend the first two years of a child's life teaching them to walk and talk...",
             "...and the next sixteen telling them to sit down and be quiet."),
            ("Every group chat has that one person who reads every message...",
             "...and replies 'k' three days later."),
            ("Why does a 'quick question' at work...", "...always need a 45-minute meeting?"),
            ("'Skip ad in 5 seconds.'", "The longest five seconds known to science."),
            ("I bought a fitness tracker to get healthier.",
             "Now I mostly walk around the room at 11:58 pm to finish my steps."),
        ],
        "Anecdotal": [
            ("A man walks into a library and asks for books on paranoia.\n"
             "The librarian leans in and whispers...", "\"They're right behind you.\""),
            ("A man tells his doctor, \"Doc, you have to help me. I'm addicted to Twitter.\"",
             "The doctor says, \"I'm sorry, I don't follow you.\""),
            ("My grandfather used the same computer for 30 years. When we finally upgraded it,\n"
             "we asked him what he'd miss the most.",
             "\"The screensaver. I thought that was the internet.\""),
            ("I tried to organise a hide-and-seek tournament at the office.\n"
             "It was going great for the first hour.",
             "Then I realised good employees are very hard to find."),
        ],
        "Situational": [
            ("Waiter: How did you find your steak, sir?", "Customer: I moved a potato and there it was."),
            ("Teacher: Why are you late?\nStudent: There was a sign outside.",
             "Student: It said 'School ahead, go slow.'"),
            ("Interviewer: Where do you see yourself in five years?",
             "Candidate: Honestly? Still waiting for you to call me back."),
            ("Boss: You're late again!", "Employee: But I left early yesterday to make up for it."),
        ],
    },
    "Hinglish": {
        "One-liner": [
            ("Mummy: Beta, padhai kar le, exam aa rahe hain.",
             "Pappu: Aane do mummy, main kaun sa unhe rokne wala hoon."),
            ("Golu: Doctor sahab, mujhe bhoolne ki bimari hai.\nDoctor: Kab se?",
             "Golu: Kab se kya?"),
            ("Customer: Waiter, is soup mein makkhi hai!",
             "Waiter: Chinta mat kijiye sir, ye zyada nahi peeyegi."),
            ("Teacher: Pappu, tum class mein so kyun rahe ho?",
             "Pappu: Sir, aapki awaaz itni meethi hai, lori jaisi lagti hai."),
            ("Golu: Mummy, kal school nahi jaunga, sar dard ho raha hai.\nMummy: Kal toh Sunday hai.",
             "Golu: Dekha! Sar dard bhi time waste kar raha hai."),
            ("Relative: Beta, aage ka kya plan hai?", "Beta: Aunty, abhi toh dinner ka plan hai."),
        ],
        "Wordplay": [
            ("Teacher: Ek saal mein kitne second hote hain?",
             "Pappu: 12 sir. 2 January, 2 February, 2 March..."),
            ("Patni: Suniye ji, aaj khana bahar khayenge.",
             "Pati: Theek hai, main chatai bahar bichha deta hoon."),
            ("Teacher: Zebra black and white kyun hota hai?",
             "Pappu: Sir, kyunki wo colour TV aane se pehle paida hua tha."),
            ("Teacher: Pappu, 'I don't know' ka matlab batao.\nPappu: Mujhe nahi pata sir.\n"
             "Teacher: Kal bhi yahi kaha tha, aaj bhi!",
             "Pappu: Toh sir, jawaab badlega thodi na?"),
            ("Teacher: Pappu, batao sabse zyada barf kahan padti hai?", "Pappu: Sir, fridge mein."),
        ],
        "Observational": [
            ("Golu ko neend nahi aa rahi thi. Dost bola: Bhed gin le.",
             "Golu: Gini yaar. 500 tak pahuncha toh subah ho gayi."),
            ("Papa: Beta, Wi-Fi ka password kya hai?",
             "Beta: Pehle apna kamra saaf karo, phir milega."),
            ("Ek machhar ne doosre se poocha: Kal shaadi mein chalega?",
             "Doosra: Nahi yaar, wahan sab log taali bajate hain. Darr lagta hai."),
            ("Biwi: Suno, main 5 minute mein tayyar hoke aati hoon.",
             "Pati: Theek hai, main tab tak naya ghar bana leta hoon."),
            ("Bachcha: Papa, mobile mein charging kahan se aati hai?\nPapa: Bijli se.",
             "Bachcha: Toh phir bijli ka bill bhi mobile wale bharte honge na?"),
            ("Har Indian ghar mein ek thaili hoti hai...", "...jiske andar aur thailiyan hoti hain."),
            ("Indian papa AC on karte hi: 'Bijli ka meter dekha hai?'",
             "Aur heater on karte hi: 'Kambal kis liye hai?'"),
        ],
        "Anecdotal": [
            ("Papa: Itne kam number kyun aaye?\nPappu: Papa, wo absent tha na.\nPapa: Kaun?",
             "Pappu: Wo ladka jiski copy dekh ke main likhta hoon."),
            ("Teacher: Homework kyun nahi kiya?\nPappu: Sir, light chali gayi thi.\n"
             "Teacher: Toh mombatti jala lete.\nPappu: Maachis mandir mein thi.\n"
             "Teacher: Toh le aate.\nPappu: Nahaya nahi tha.\nTeacher: Kyun nahi nahaye?",
             "Pappu: Paani nahi tha sir, motor light se chalti hai."),
            ("Shaadi mein Golu ne teen baar khana khaya. Caterer ne pakad liya:\n"
             "'Aap ladke wale ho ya ladki wale?'", "Golu: 'Bhaiya, main khane wala hoon.'"),
            ("Sharma ji ne naya smart speaker liya. Pehle din bole 'Hey Google', doosre din 'OK Google',\n"
             "teesre din gusse mein 'Arre Google, sunta kyun nahi!'",
             "Chauthe din speaker bola: 'Uncle, main Alexa hoon.'"),
        ],
        "Situational": [
            ("Interviewer: Aapki sabse badi kamzori kya hai?\n"
             "Candidate: Main bahut imaandaar hoon.\n"
             "Interviewer: Mujhe nahi lagta ye kamzori hai.",
             "Candidate: Mujhe aapki rai ki parwah bhi nahi hai."),
            ("Teacher: Agar tumhare paas 10 aam hain aur main 5 maang loon, toh kitne bachenge?",
             "Pappu: 10 hi sir. Main dunga hi nahi."),
            ("TT: Ye ticket toh bachche ka hai!",
             "Pappu: Toh dekh lijiye, aapki train ne kitna intezaar karwaya."),
            ("Golu library mein: Bhaiya, ek burger aur fries dena.\nLibrarian: Ye library hai!",
             "Golu (dheere se): Sorry... ek burger aur fries dena."),
            ("Doctor: Aapko roz subah 5 km walk karni chahiye.\nMareez: Ji, ek mahine baad phone karunga.",
             "Doctor: Kyun? Mareez: Tab tak main 150 km door pahunch jaunga."),
        ],
    },
}

# ---------------------------------------------------------------------------
# Joke sources
# ---------------------------------------------------------------------------

SOURCE_AUTO = "Auto (best available)"
SOURCE_WEB = "Joke websites"
SOURCE_BUILTIN = "Built-in collection"
ENGINE_GROQ = "Groq AI"
ENGINE_HF = "Hugging Face AI"
PROVIDERS = {ENGINE_GROQ: jokeapp_groq, ENGINE_HF: jokeapp_hf}


def make_joke(setup, punch, source, lang, jtype):
    return {"setup": setup.strip(), "punch": punch.strip(), "source": source,
            "lang": lang, "type": jtype, "rating": None}


def pick_builtin(lang, jtype):
    """Random built-in joke of the chosen type. No repeats until the list runs out."""
    types = list(JOKE_TYPES) if jtype == RANDOM else [jtype]
    catalogue = [(t, i) for t in types for i in range(len(JOKES[lang][t]))]
    key = f"{lang}|{jtype}"
    pool = st.session_state.pools.setdefault(key, [])
    if not pool:
        pool.extend(random.sample(catalogue, len(catalogue)))
    t, i = pool.pop()
    setup, punch = JOKES[lang][t][i]
    return make_joke(setup, punch, SOURCE_BUILTIN, lang, t)


def fetch_web_english(jtype):
    """JokeAPI (Pun category for Wordplay), then Official Joke API for Random."""
    category = "Pun" if jtype == "Wordplay" else "Any"
    try:
        r = requests.get(config.JOKEAPI_URL.format(category=category),
                         params={"safe-mode": "", "type": "twopart"},
                         timeout=config.REQUEST_TIMEOUT)
        data = r.json() if r.status_code == 200 else {}
        if data and not data.get("error"):
            label = "Wordplay" if data.get("category") == "Pun" else "Mixed"
            return make_joke(data["setup"], data["delivery"], "JokeAPI", "English", label)
    except (requests.RequestException, ValueError, KeyError):
        pass

    if jtype == RANDOM:
        try:
            r = requests.get(config.OFFICIAL_JOKE_URL, timeout=config.REQUEST_TIMEOUT)
            if r.status_code == 200:
                data = r.json()
                return make_joke(data["setup"], data["punchline"], "Official Joke API",
                                 "English", "Mixed")
        except (requests.RequestException, ValueError, KeyError):
            pass
    return None


def ask_ai(module, lang, jtype, avoid):
    """Works with the current provider files and picks up joke types once they support them.

    Preferred:  module.get_joke(language=..., style=..., avoid=...)
    Fallback:   module.get_hinglish_joke(avoid=..., [style=...])
    """
    style = None if jtype == RANDOM else f"{jtype} - {JOKE_TYPES[jtype][1]}"
    if hasattr(module, "get_joke"):
        return module.get_joke(language=lang, style=style, avoid=avoid)
    if lang == "Hinglish":
        fn = module.get_hinglish_joke
        kwargs = {"avoid": avoid}
        if style and "style" in inspect.signature(fn).parameters:
            kwargs["style"] = style
        return fn(**kwargs)
    raise RuntimeError("This AI source only writes Hinglish jokes right now")


def available_ai():
    return [name for name, mod in PROVIDERS.items() if mod.is_available()]


def source_options(lang):
    opts = [SOURCE_AUTO]
    if lang == "English":
        opts.append(SOURCE_WEB)
    return opts + available_ai() + [SOURCE_BUILTIN]


def get_joke(source, lang, jtype):
    st.session_state.notice = None
    recent = st.session_state.recent_setups

    plan = []
    if source == SOURCE_AUTO:
        if lang == "English" and jtype in (RANDOM, "Wordplay"):
            plan.append(SOURCE_WEB)
        plan += available_ai()
    elif source != SOURCE_BUILTIN:
        plan.append(source)

    for step in plan:
        try:
            if step == SOURCE_WEB:
                joke = fetch_web_english(jtype)
            else:
                setup, punch = ask_ai(PROVIDERS[step], lang, jtype, recent[-10:])
                joke = make_joke(setup, punch, step, lang,
                                 "Surprise" if jtype == RANDOM else jtype)
            if joke:
                recent.append(joke["setup"][:80])
                del recent[:-20]
                return joke
        except Exception as exc:  # any provider hiccup -> try the next source
            if source != SOURCE_AUTO:
                st.session_state.notice = f"{step}: {str(exc).rstrip('.')}"
    if source not in (SOURCE_AUTO, SOURCE_BUILTIN) and not st.session_state.notice:
        st.session_state.notice = f"{source} didn't return a joke"
    return pick_builtin(lang, jtype)


# ---------------------------------------------------------------------------
# State and callbacks
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Hasi Mazaak", page_icon="😂", layout="centered")

for k, v in {"joke": None, "revealed": False, "count": 0, "laughs": 0, "history": [],
             "favorites": [], "recent_setups": [], "pools": {}, "notice": None,
             "jtype": RANDOM}.items():
    st.session_state.setdefault(k, v)

RATINGS = {"haha": "😂", "ok": "🙂", "meh": "😐"}


def set_type(name):
    st.session_state.jtype = name


def reveal():
    st.session_state.revealed = True


def rate(value):
    joke = st.session_state.joke
    if joke["rating"] == "haha":
        st.session_state.laughs -= 1
    joke["rating"] = None if joke["rating"] == value else value
    if joke["rating"] == "haha":
        st.session_state.laughs += 1


def toggle_favorite():
    joke, favs = st.session_state.joke, st.session_state.favorites
    if joke in favs:
        favs.remove(joke)
    else:
        favs.append(joke)


def remove_favorite(idx):
    st.session_state.favorites.pop(idx)


def joke_as_text(j):
    return f"{j['setup']}\n{j['punch']}"


# ---------------------------------------------------------------------------
# Styles - CSS only. All page content below uses plain Streamlit components;
# containers with a key= get a ".st-key-<key>" class that the CSS targets.
# ---------------------------------------------------------------------------

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;800&family=Nunito:wght@400;600;700&display=swap');

:root { --ink:#2b1a3d; --marigold:#f7a928; --rani:#e0367a; --paper:#fff8ec; --muted:#7a6a86; }
.stApp { background: radial-gradient(circle at 15% 0%, #ffe3b0 0%, var(--paper) 45%); }
html, body, p, label, li { font-family:'Nunito',sans-serif; color:var(--ink); }

h1, h3, h4 { font-family:'Baloo 2',cursive !important; color:var(--ink) !important; }
h1 { font-weight:800 !important; font-size:3.2rem !important; padding-bottom:0 !important; }
h4 { font-weight:800 !important; padding-top:.8rem !important; }

/* Joke card */
.st-key-joke_card { background:#fff; border:3px solid var(--ink) !important; border-radius:22px !important;
                    box-shadow:8px 8px 0 var(--marigold); padding:1.4rem 1.6rem 1rem !important; }
.st-key-setup [data-testid="stText"], .st-key-punch [data-testid="stText"] {
    font-family:'Baloo 2',cursive; white-space:pre-wrap; line-height:1.35; color:var(--ink); }
.st-key-setup [data-testid="stText"] { font-size:1.4rem; font-weight:600; }
.st-key-punch [data-testid="stText"] { font-size:1.5rem; font-weight:800; color:var(--rani);
                                       animation:pop .35s ease-out; }
@keyframes pop { from { transform:scale(.9); opacity:0; } to { transform:scale(1); opacity:1; } }
@media (prefers-reduced-motion: reduce) { .st-key-punch [data-testid="stText"] { animation:none; } }

/* Favourites in the sidebar */
[class*="st-key-fav_"] { background:#fff; border-left:4px solid var(--rani) !important; border-radius:12px !important; }
[class*="st-key-fav_"] [data-testid="stText"] { white-space:pre-wrap; font-family:'Nunito',sans-serif; font-size:.9rem; }

/* Stats */
[data-testid="stMetric"] { background:#fff; border:2px solid var(--ink); border-radius:14px; padding:.4rem .6rem; text-align:center; }
[data-testid="stMetricValue"] { font-family:'Baloo 2',cursive; }

/* Buttons */
div.stButton > button { border-radius:999px; border:2px solid var(--ink);
    font-family:'Baloo 2',cursive; font-weight:600; font-size:1.02rem; }
div.stButton > button[kind="primary"] { background:var(--ink); color:#fff; }
div.stButton > button[kind="primary"]:hover { background:var(--rani); border-color:var(--rani); color:#fff; }
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)  # the one place a tag is needed: loading CSS

# ---------------------------------------------------------------------------
# Sidebar: settings, stats, favourites, history
# ---------------------------------------------------------------------------

lang_now = st.session_state.get("language", "English")
with st.sidebar:
    st.subheader("⚙️ Settings")
    source = st.selectbox("Joke source", source_options(lang_now), key="source",
                          help="Auto tries joke websites and AI first, and falls back to the built-in collection.")
    auto_reveal = st.toggle("Show punchline straight away", key="auto_reveal")
    if not available_ai():
        st.caption("Add GROQ_API_KEY or HF_TOKEN to your .env file for fresh AI-written jokes.")

    st.subheader("📊 Today")
    s1, s2, s3 = st.columns(3)
    s1.metric("Jokes", st.session_state.count)
    s2.metric("😂", st.session_state.laughs)
    s3.metric("⭐", len(st.session_state.favorites))

    st.subheader("⭐ Favourites")
    favs = st.session_state.favorites
    if not favs:
        st.caption("Tap ☆ Save on a joke you like and it lands here.")
    for i, f in enumerate(favs):
        with st.container(border=True, key=f"fav_{i}"):
            st.text(joke_as_text(f))
            st.button("Remove", key=f"rm_{i}", on_click=remove_favorite, args=(i,))
    if favs:
        st.download_button(
            "⬇️ Download favourites",
            "\n\n".join(f"[{f['type']} · {f['lang']}]\n{joke_as_text(f)}" for f in favs),
            file_name="hasi_mazaak_favourites.txt", use_container_width=True)

    history = st.session_state.history
    if history:
        with st.expander(f"🕘 Recent jokes ({len(history)})"):
            for h in reversed(history[-10:]):
                short = h["setup"].replace("\n", " ")
                st.text(f"{RATINGS.get(h['rating'], '·')} {short[:60]}{'…' if len(short) > 60 else ''}")

# ---------------------------------------------------------------------------
# Main page
# ---------------------------------------------------------------------------

st.title("Hasi Mazaak 😂")
st.caption("Ek joke, do bhashayein. One tap, one laugh.")

# Step 1: language
st.markdown("#### 1 · Pick a language")
language = st.radio("Language", ["English", "Hinglish"], horizontal=True, key="language",
                    label_visibility="collapsed",
                    format_func=lambda x: "🇬🇧 English" if x == "English" else "🇮🇳 Hinglish")
hi = language == "Hinglish"

# Step 2: joke type
st.markdown("#### 2 · Pick a joke type")
type_names = [RANDOM] + list(JOKE_TYPES)
cols = st.columns(3)
for i, name in enumerate(type_names):
    with cols[i % 3]:
        st.button(f"{TYPE_ICONS[name]} {name}", key=f"type_{name}", use_container_width=True,
                  type="primary" if st.session_state.jtype == name else "secondary",
                  on_click=set_type, args=(name,))
jtype = st.session_state.jtype
st.caption(f"{TYPE_ICONS[jtype]} **{jtype}** · "
           f"{'Any type - surprise me.' if jtype == RANDOM else JOKE_TYPES[jtype][1]}")

# Step 3: joke
st.markdown("#### 3 · Get your joke")
joke = st.session_state.joke
b1, b2 = st.columns(2)
with b1:
    if joke is None:
        label = "Joke sunao!" if hi else "Tell me a joke"
    else:
        label = "Ek aur! 🔁" if hi else "Another one 🔁"
    if st.button(label, type="primary", use_container_width=True, key="new_joke"):
        with st.spinner("Joke soch raha hoon..." if hi else "Cooking up a joke..."):
            joke = get_joke(source, language, jtype)
        st.session_state.joke = joke
        st.session_state.revealed = auto_reveal
        st.session_state.count += 1
        st.session_state.history.append(joke)
        del st.session_state.history[:-25]
with b2:
    st.button("Punchline batao! 🥁" if hi else "Show punchline 🥁", use_container_width=True,
              key="reveal", on_click=reveal,
              disabled=joke is None or st.session_state.revealed)

with st.container(border=True, key="joke_card"):
    if joke is None:
        st.markdown("**Ready when you are.**")
        st.caption("Pick a language and a joke type, then hit “Tell me a joke”.")
    else:
        revealed = st.session_state.revealed
        st.caption(f"{TYPE_ICONS.get(joke['type'], '🎲')} {joke['type']} · {joke['lang']}")
        with st.container(key="setup"):
            st.text(joke["setup"])
        if revealed:
            with st.container(key="punch"):
                st.text(joke["punch"])
        else:
            st.caption("Socho, socho..." if hi else "Have a guess...")
        st.caption(f"Joke #{st.session_state.count} · {joke['source']}")

if joke is not None:
    if st.session_state.notice:
        st.caption(f"⚠️ {st.session_state.notice}. Showing a built-in joke instead.")

    if st.session_state.revealed:
        r1, r2, r3, r4 = st.columns(4)
        for col, (key, emoji), text in zip((r1, r2, r3), RATINGS.items(),
                                           ("Haha", "Theek hai" if hi else "Okay", "Meh")):
            col.button(f"{emoji} {text}", key=f"rate_{key}", use_container_width=True,
                       type="primary" if joke["rating"] == key else "secondary",
                       on_click=rate, args=(key,))
        saved = joke in st.session_state.favorites
        r4.button("⭐ Saved" if saved else "☆ Save", key="fav", use_container_width=True,
                  type="primary" if saved else "secondary", on_click=toggle_favorite)
        with st.expander("📋 Copy / share this joke"):
            st.code(joke_as_text(joke), language=None)