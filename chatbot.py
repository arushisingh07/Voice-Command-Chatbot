import speech_recognition as sr
import sounddevice as sd
import numpy as np
import webbrowser

def listen_command():
    recognizer = sr.Recognizer()
    duration = 5  # seconds to record
    fs = 44100  # sample rate

    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished

    # Convert the NumPy array to audio data bytes
    audio_data = np.int16(recording * 32767).tobytes()
    audio = sr.AudioData(audio_data, fs, 2)  # 2 bytes per sample (16-bit audio)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return ""

def execute_command(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube...")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        print("Opening Google...")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        print("Opening Facebook...")
    else:
        print("Command not recognized.")

if __name__ == "__main__":
    print("Say 'exit' or 'quit' to stop.")
    while True:
        cmd = listen_command()
        if cmd:
            if "exit" in cmd or "quit" in cmd:
                print("Exiting...")
                break
            execute_command(cmd)