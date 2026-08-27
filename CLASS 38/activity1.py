import speech_recognition as sr
from deep_translator import GoogleTranslator
import subprocess


def speak(text, language="en"):
    # macOS voice settings
    voices = {
        "en": "Samantha",
        "hi": "Lekha",
        "ta": "Vani",
        "te": "Samantha",
        "bn": "Samantha",
        "mr": "Lekha",
        "gu": "Lekha",
        "ml": "Samantha",
        "pa": "Lekha"
    }

    voice = voices.get(language, "Samantha")

    try:
        subprocess.run(["say", "-v", voice, text])
    except Exception as e:
        print(f"❌ Voice error: {e}")


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("🔎 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")

    except sr.RequestError as e:
        print(f"❌ API Error: {e}")

    return ""


def translate_text(text, target_language):
    try:
        translation = GoogleTranslator(
            source="en",
            target=target_language
        ).translate(text)

        print(f"🌐 Translated text: {translation}")
        return translation

    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return text


def display_language_options():
    print("\n🌐 Available translation languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")

    choice = input("\nPlease select the target language number (1-8): ")

    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }

    return language_dict.get(choice, "hi")


def main():
    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(
            original_text,
            target_language
        )

        print("🔊 Speaking translation...")
        speak(translated_text, target_language)

        print("✅ Translation spoken out!")


if __name__ == "__main__":
    main()