# VoiceLauncher

VoiceLauncher is a local, offline voice-activated automation tool built in Python. It uses **Vosk** for speech recognition and **sounddevice** for real-time microphone input. The system listens continuously, detects a **wake word** ("activate"), and then waits for a **clap** to trigger an action.

Current behavior:

* Listens to the microphone
* Detects the wake word **activate**
* After wake word detection, waits for a clap
* On clap, creates a new project folder and opens it in VS Code (optional)

The design intentionally avoids cloud APIs and runs fully offline.

---

## Project Structure

```
VoiceLauncher/
│
├── main.py                     # Core application logic
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── vosk-model-small-en-us-0.15/ # Speech recognition model (NOT committed)
└── .venv/                       # Python virtual environment (NOT committed)
```

---

## Requirements

* Python **3.9 – 3.11** (recommended)
* Windows (tested on Windows 10/11)
* Microphone

Python packages:

* vosk
* sounddevice
* numpy
* pyautogui (optional, for UI automation)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd VoiceLauncher
```

---

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install vosk sounddevice numpy pyautogui
```

If `sounddevice` fails to install, install PortAudio:

```bash
pip install pipwin
pipwin install pyaudio
```

---

### 4. Download the Vosk model

Download:

* **vosk-model-small-en-us-0.15**

From the official Vosk models page.

Extract the folder so the structure looks like:

```
VoiceLauncher/
├── main.py
├── vosk-model-small-en-us-0.15/
│   ├── am/
│   ├── conf/
│   └── ...
```

The model folder must be **next to ****************************`main.py`**.

---

### 5. Verify `.gitignore`

Ensure these are ignored:

```
.venv/
vosk-model-small-en-us-0.15/
__pycache__/
*.log
```

---

## Running the Project

Activate the virtual environment, then:

```bash
python main.py
```

Expected output:

```
Listening for claps...
PARTIAL: activate
WAKE WORD DETECTED
CLAP DETECTED
DETECTED - Opening VS Code in C:\Users\...\Project_19_01
```

---

##

##

---
