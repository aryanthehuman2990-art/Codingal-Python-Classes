import random

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️ Run: pip install pyttsx3")


def setup_tts():
    if not TTS_AVAILABLE:
        return None

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.9)
        return engine
    except Exception as e:
        print("❌ TTS error:", e)
        return None


def speak(engine, text):
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("❌ Speaking error:", e)
    else:
        print(f"🔊 [AUDIO]: {text}")


def get_samples():
    return [
        "Hello! I am your computer!",
        "Python is awesome!",
        "This is AI speaking!",
        "Welcome to the future!"
    ]


def main():
    print("🤖 AI VOICE LAB")
    print("===============")

    engine = setup_tts()

    if engine:
        print("✅ Voice ready! Try typing something...")
    else:
        print("⚠️ No audio, but you can still learn!")

    speak(engine, "Hello! Type something for me to say!")

    while True:
        text = input("\n👤 You: ").strip()

        if text.lower() == "exit":
            speak(engine, "Goodbye!")
            break

        elif text.lower() == "sample":
            phrase = random.choice(get_samples())
            print(f"💬 {phrase}")
            speak(engine, phrase)

        elif text == "":
            print("💡 Type something for me to say!")

        else:
            print(f"🔊 Saying: {text}")
            speak(engine, text)


if __name__ == "__main__":
    main()