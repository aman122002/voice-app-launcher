import sounddevice as sd
import numpy as np

def audio_callback(indata, frames, time, status):
    volume = np.linalg.norm(indata)
    print(volume)

with sd.InputStream(channels=1, samplerate=16000, callback=audio_callback):
    print("Listening...")
    while True:
        pass
