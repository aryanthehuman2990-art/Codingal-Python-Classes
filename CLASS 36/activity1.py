
import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()
MAX_RECORD_SECONDS = 120  # safety net so it can't run forever


def wait_for_enter():
    try:
        input("\n🎤 Press Enter to stop recording...\n")
    except EOFError:
        pass
    stop_event.set()


def spinner():
    chars = '|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f'\r🔴 Recording... {chars[i % 4]}')
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r✅ Recording complete!          ")


def record_audio():
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                         input=True, frames_per_buffer=1024)
    except OSError as e:
        p.terminate()
        print(f"❌ Could not open microphone: {e}")
        sys.exit(1)

    frames = []
    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()

    start_time = time.time()
    while not stop_event.is_set():
        try:
            frames.append(stream.read(1024, exception_on_overflow=False))
        except OSError as e:
            print(f"\n⚠️ Read error, stopping: {e}")
            break
        if time.time() - start_time > MAX_RECORD_SECONDS:
            print(f"\n⏱️ Max recording length ({MAX_RECORD_SECONDS}s) reached.")
            stop_event.set()

    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()

    if not frames:
        print("❌ No audio captured.")
        sys.exit(1)

    return b''.join(frames), 16000, width


def save_audio(data, rate, width, filename="recording.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"💾 Saved: {filename}")


def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(data, rate, width)
    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 Transcription: {text}")
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")


def plot_waveform(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    if len(samples) == 0:
        print("⚠️ No samples to plot.")
        return
    time_axis = np.linspace(0, len(samples) / rate, len(samples))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, samples, color='blue')
    plt.title("Your Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    print("=" * 40)
    print("🎙️  HELLO AI, CAN YOU HEAR ME?")
    print("=" * 40)
    print("\nSpeak into your microphone...")

    try:
        audio_data, rate, width = record_audio()
        save_audio(audio_data, rate, width)
        transcribe(audio_data, rate, width)
        plot_waveform(audio_data, rate)
    except KeyboardInterrupt:
        print("\n👋 Interrupted, exiting.")
        sys.exit(0)


if __name__ == "__main__":
    main()