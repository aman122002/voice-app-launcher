import sounddevice as sd
import numpy as np
import time
import subprocess
import os
from datetime import datetime
import pyautogui
from vosk import Model, KaldiRecognizer
import queue
import json


# Clap detection parameters
CLAP_THRESHOLD = 11.0  # adjust until it triggers reliably
COOLDOWN = 5.0       # minimum seconds between claps
last_clap = 0         # last clap timestamp
wake_word = False

q = queue.Queue()

# Get folder where main.py is located
base_dir = os.path.dirname(__file__)

# Relative path to the model
model_path = os.path.join(base_dir, "vosk-model-small-en-us-0.15")

# Load model
model = Model(model_path)
recognizer = KaldiRecognizer(
    model,
    16000,
    '["activate"]'
)

def audio_callback(indata, frames, time_info, status):
    global last_clap, wake_word
    # Convert float32 → int16 PCM
    pcm16 = (indata * 32767).astype(np.int16)

    q.put(pcm16.tobytes())

    volume = np.linalg.norm(indata)
    now = time.time()

    # Detect a clap
    if wake_word and volume > CLAP_THRESHOLD and now - last_clap > COOLDOWN :
        last_clap = now
        time_stamp = datetime.now().strftime("%d_%m")
        wake_word = False
        # print(time_stamp)
        print("CLAP DETECTED")
        # Trigger action: open VS Code
        project_folder = os.path.join(os.path.expanduser("~\\Desktop\\VoiceProjects"), f"Project_{time_stamp}")
        os.makedirs(project_folder, exist_ok=True)
        print(f"DETECTED - Opening VS Code in {project_folder}")

        # Launch VS Code
        subprocess.Popen(f'code "{project_folder}"', shell=True)

        # Wait a moment for VS Code to open
        time.sleep(2)

        # Press F11 to enter full-screen
        pyautogui.press('f11')



# Start microphone stream
with sd.InputStream(channels=1, samplerate=16000, dtype="float32", callback=audio_callback):
    print("Listening for claps...")
    while True:
        data = q.get()  # blocking, safer than q.empty()

        recognizer.AcceptWaveform(data)

        partial = json.loads(recognizer.PartialResult())
        partial_text = partial.get("partial", "")

        if partial_text:
            print("PARTIAL:", partial_text)

            if "activate" in partial_text.lower():
                wake_word = True
                wake_time =  time.time()
                print("WAKE WORD DETECTED")
                recognizer.Reset()

        
        