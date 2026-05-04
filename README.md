# 🍅 Pomodoro Desktop App

A modern cross-platform Pomodoro timer built with Python and PyQt6.

Designed for focused work sessions, clean UI, and future extensibility.

---

## ✨ Features

* ⏱️ 25 / 5 Pomodoro workflow
* ▶️ Start, Pause, Reset controls
* 🌙 Dark theme UI
* 🖥️ Cross-platform support:

  * Windows
  * macOS
* 🎯 Minimal and distraction-free interface
* 📦 Standalone executable support

---

## 📸 Screenshot

![Pomodoro App](assets/screenshot.png)

*Add application screenshot here*

```md
![Pomodoro Screenshot](assets/screenshot.png)
```

---

## 🛠️ Tech Stack

Built with:

* Python 3.11+
* PyQt6
* qt-material

---

## 📂 Project Structure

```text
pomodoro-app/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── screenshot.png
│
├── build/        # local only
├── dist/         # local only
└── venv/         # local only
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/pomodoro-app.git
cd pomodoro-app
```

Create virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python main.py
```

---

## 📦 Build Executable

Using PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
pyinstaller --onefile --windowed main.py
```

Output will be generated in:

```text
dist/
```

---

## 🔮 Planned Features

* 🔔 Native notifications
* 📊 Session statistics
* 📝 Task tracking
* 💾 Session persistence
* ⚙️ Custom timer settings
* 🔄 Auto-start next session

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome.

Feel free to open an issue or submit a pull request.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Built by Stelian Radu.
