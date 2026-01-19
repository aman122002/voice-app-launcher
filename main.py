import sounddevice as sd
import numpy as np
import time
import subprocess

# Clap detection parameters
CLAP_THRESHOLD = 0.6  # adjust until it triggers reliably
COOLDOWN = 1.5        # minimum seconds between claps
last_clap = 0         # last clap timestamp

def audio_callback(indata, frames, time_info, status):
    global last_clap
    volume = np.linalg.norm(indata)
    now = time.time()

    # Detect a clap
    if volume > CLAP_THRESHOLD and now - last_clap > COOLDOWN:
        last_clap = now
        print("CLAP DETECTED")
        # Trigger action: open VS Code
        subprocess.Popen("code", shell=True)  # assumes 'code' command works in terminal

# Start microphone stream
with sd.InputStream(channels=1, samplerate=16000, callback=audio_callback):
    print("Listening for claps...")
    while True:
        pass
