````markdown
# 🎙️ Wayland-Compatible Linux Voice Assistant

A simple, Python-based voice assistant that listens for commands, responds using text-to-speech, performs actions like typing using `ydotool`, and more. Built for Wayland environments such as Hyprland, Sway, or GNOME Wayland.

---

## 🧠 Features

- 🗣️ Voice command recognition via Google Speech API
- 🧾 Task management (add/list tasks)
- 📸 Take screenshots (via `grim`)
- 🌐 Open websites (e.g., YouTube)
- ⌨️ Type text using `ydotool`
- 🔊 Responds using `gTTS` and `ffplay` (no GUI dependency)
- 🪟 Fully compatible with Wayland (no `pyautogui` required)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/linux-voice-assistant.git
cd linux-voice-assistant
````

### 2. Set Up Virtual Environment

```bash
python3 -m venv assistant_env
source assistant_env/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install System Dependencies (Linux)

```bash
sudo apt update && sudo apt install \
    portaudio19-dev ffmpeg ydotool grim \
    libasound-dev libpulse-dev libgirepository1.0-dev
```

---

## 🧪 Usage

### Start the Assistant

```bash
python3 assistant.py
```

### Trigger Word

Say: `Radhe` followed by one of the supported commands.

### Supported Commands

* `"Radhe, add a task"` → Adds a task to your task list
* `"Radhe, list tasks"` → Reads out your tasks
* `"Radhe, take a screenshot"` → Saves screenshot as `screenshot.png`
* `"Radhe, open chrome"` → Opens YouTube in the default browser
* `"Radhe, type <your text>"` → Types text using `ydotool`
* `"Radhe, exit"` → Exits the assistant

---

## 🔧 How It Works

* **Speech Recognition**: `speech_recognition` listens to the microphone and uses Google API.
* **TTS**: `gTTS` converts text to audio, played via `ffplay`.
* **Keyboard Input**: `ydotool` is used instead of `pyautogui` for Wayland compatibility.
* **Screenshot**: `grim` captures screenshots (Wayland alternative to `scrot`).

---

## 🖥️ Demo

> Add a GIF or YouTube video link here showing the assistant in action.

---

## 🛠️ Project Structure

```
.
├── assistant.py          # Main voice assistant script
├── requirements.txt      # Python dependencies
├── README.md             # You're reading it!
```

---

## 💡 Troubleshooting

* ❌ `ModuleNotFoundError: No module named 'pyaudio'`
  → Run: `sudo apt install portaudio19-dev` then `pip install pyaudio`

* ❌ `playsound error with gi`
  → Use `ffplay` method instead of `playsound`

* ❌ `ydotool: command not found`
  → Run: `sudo apt install ydotool` (must have `uinput` permissions)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to open an issue or create a feature request.

---

## 👤 Author

* **Tanya Mishra** – [GitHub](https://github.com/tanya1280mishra) | [LinkedIn](https://linkedin.com/in/tanya-mishra-bit)

