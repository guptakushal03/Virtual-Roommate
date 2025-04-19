Here's a clean and informative `README.md` you can include with your **Virtual Roommate** project:

---

# 🧠 Virtual Roommate

**Virtual Roommate** is a friendly desktop companion that keeps you on track with randomized reminders based on your selected "personality" — **Zen** or **Gremlin**. It lives in your system tray, giving nudges, encouragement, or chaos (depending on your mood).

![Tray Icon Example](https://img.icons8.com/?size=80&id=KzZwUfg10Axy&format=png)  
*Get reminded to drink water, stretch, or just... vibe.*

---

## ✨ Features

- 🔔 Random reminder popups at customizable intervals
- 🎭 Switch between **Zen** and **Gremlin** personalities
- 💬 Voice + Toast notifications
- 👀 Detects AFK (away-from-keyboard) state to pause reminders
- 🖱️ Runs silently in system tray
- 🧠 Modular personality & quote structure

---

## 📦 Installation

1. Clone or download the repo.
2. Make sure `Python 3.10+` is installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your **custom quotes** in `roommate_quotes.py`.

---

## 🔧 Build Executable (Windows Only)

To create a standalone `.exe` with all files bundled (no external dependencies):

```bash
pyinstaller main.py --name "VirtualRoommate" --icon=icon.ico --noconsole --onefile --add-data "icon.ico;."
```

> 🔁 For development, just run `python main.py`

---

## 🧩 File Structure

```
📁 VirtualRoommate/
├── main.py                  # Main app
├── roommate_quotes.py       # All quotes & interval logic
├── afk_checker.py           # Detects user activity
├── icon.ico                 # Tray icon
├── README.md
└── requirements.txt
```

---

## 🎭 Personalities

- **Gremlin**: Chaotic & hilarious reminders like _"Posture? Nah. Become shrimp."_
- **Zen**: Calmer nudges like _"Take a breath. Your peace matters."_

Easily switch personalities from the tray icon.

---

## 🛑 Quit App

Right-click on the tray icon → `Quit`

---

## 🐛 Troubleshooting

If anything breaks, an `error.log` file will be created in the same directory with the stack trace.

### Common Gotchas:
- **Missing icon.ico?** Make sure it's bundled correctly with `--add-data`.
- **Executable doesn't run?** Try using `--onefile --noconsole` and test without `pyttsx3` first.

---

## 📜 License

MIT — Customize, break, and enhance it however you want!

---

Let me know if you'd like to add:
- Screenshots
- More personalities
- GitHub badges or links

Want me to generate the `requirements.txt` too?
