import sounddevice as sd
import numpy as np
import time
import subprocess
import os
from datetime import datetime
import pyautogui


# Clap detection parameters
CLAP_THRESHOLD = 11.0  # adjust until it triggers reliably
COOLDOWN = 1.0       # minimum seconds between claps
last_clap = 0         # last clap timestamp

def audio_callback(indata, frames, time_info, status):
    global last_clap
    volume = np.linalg.norm(indata)
    now = time.time()

    # Detect a clap
    if volume > CLAP_THRESHOLD and now - last_clap > COOLDOWN:
        last_clap = now
        print(volume)
        time_stamp = datetime.now().strftime("%d_%m")
        # print(time_stamp)
        print("CLAP DETECTED")
        # Trigger action: open VS Code
        project_folder = os.path.join(os.path.expanduser("~\\Desktop\\VoiceProjects"), f"Project_{time_stamp}")
        os.makedirs(project_folder, exist_ok=True)
        print(f"CLAP DETECTED - Opening VS Code in {project_folder}")

        # Launch VS Code
        subprocess.Popen(f'code "{project_folder}"', shell=True)

        # Wait a moment for VS Code to open
        time.sleep(2)

        # Press F11 to enter full-screen
        pyautogui.press('f11')



# Start microphone stream
with sd.InputStream(channels=1, samplerate=16000, callback=audio_callback):
    print("Listening for claps...")
    while True:
        pass
