import io
import time
import speech_recognition as sr
from gtts import gTTS
import pygame
from googletrans import Translator


def speak(text, language="en"):
    """Convert text to speech using gTTS and play it directly from memory
    (no file written to disk, no player window)."""
    if not text:
        print("Nothing to speak.")
        return

    try:
        tts = gTTS(text=text, lang=language)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
    except Exception as e:
        print(f"Error generating speech (check internet connection / language code): {e}")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_fp, "mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.quit()
    except Exception as e:
        print(f"Error playing audio: {e}")


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in English...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return None


def translate_text(text, target_language="es"):
    """Translate text using googletrans. Returns None if translation fails."""
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        print(f"Translated text: {translation.text}")
        return translation.text
    except Exception as e:
        print("Translation error (googletrans is unreliable - consider switching")
        print(f"to the 'deep-translator' package if this keeps happening): {e}")
        return None


def display_language_options():
    print("Available translation languages:")
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

    if not original_text:
        print("No speech was recognized, so nothing was translated.")
        return

    translated_text = translate_text(original_text, target_language=target_language)

    if not translated_text:
        print("Translation failed, so nothing was spoken.")
        return

    speak(translated_text, language=target_language)
    print("Translation spoken out!")


if __name__ == "__main__":
    main()