import speech_recognition as sr
from gtts import gTTS
import os
import time
from googletrans import Translator


def speak(text, language="en"):
    """Convert text to speech using gTTS (supports Hindi, Tamil, etc.) and play it."""
    try:
        tts = gTTS(text=text, lang=language)
        filename = "output.mp3"
        tts.save(filename)

        # Play the audio file (Windows). Use "afplay" on Mac, "mpg123"/"xdg-open" on Linux.
        os.system(f"start {filename}")

        # Small delay so the file isn't deleted before playback starts
        time.sleep(1)
    except Exception as e:
        print(f"⚠️ Error while speaking: {e}")


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        audio = recognizer.listen(source)
    try:
        print("🔎 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")  # English recognition
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return None


def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌐 Translated text: {translation.text}")
    return translation.text


def display_language_options():
    print("🌍 Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    choice = input("Please select the target language number (1-8): ")
    language_dict = {
        "1": "hi", "2": "ta", "3": "te", "4": "bn",
        "5": "mr", "6": "gu", "7": "ml", "8": "pa"
    }
    return language_dict.get(choice, "es")


def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
        # Use target_language here (NOT hardcoded "en") so the correct voice/language is used
        speak(translated_text, language=target_language)
        print("✅ Translation spoken out!")
    else:
        print("⚠️ No speech was recognized, so nothing was translated.")


if __name__ == "__main__":
    main()
