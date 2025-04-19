import time
import threading
import random
from pystray import Icon, Menu, MenuItem
from PIL import Image
from win10toast_click import ToastNotifier
import pyttsx3
from roommate_quotes import reminder_categories
from afk_checker import start_input_listener, afk_monitor_loop
import wmi


current_personality = "gremlin"
running = True
toaster = ToastNotifier()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def show_reminder(quote, category):
    toaster.show_toast(
        f"{category.capitalize()} Reminder",
        quote,
        icon_path=resource_path("icon.ico"),
        duration=10,
        threaded=True
    )
    speak_message(quote)

def reminder_loop(category, interval_range):
    while running:
        delay = random.randint(*interval_range)
        time.sleep(delay)
        if running:
            quote = random.choice(reminder_categories[category]["quotes"][current_personality])
            show_reminder(quote, category)

def start_reminder_threads():
    for category, data in reminder_categories.items():
        threading.Thread(
            target=reminder_loop,
            args=(category, data["interval_range"]),
            daemon=True
        ).start()

def toggle_personality(icon, item):
    global current_personality
    current_personality = "zen" if current_personality == "gremlin" else "gremlin"
    toaster.show_toast(
        "Virtual Roommate",
        f"Switched to {current_personality.title()} mode!",
        icon_path=resource_path("icon.ico"),
        duration=5,
        threaded=True
    )

def exit_app(icon, item):
    global running
    running = False
    icon.stop()

def setup_tray():
    image = Image.open(resource_path("icon.ico"))
    start_input_listener()
    threading.Thread(target=afk_monitor_loop, args=(lambda: current_personality,), daemon=True).start()
    start_reminder_threads()

    welcome_messages = {
        "gremlin": "Let’s ruin your posture together",
        "zen": "Welcome back. Let’s stay balanced today"
    }

    welcome_message = welcome_messages[current_personality]
    toaster.show_toast(
        "Virtual Roommate",
        welcome_message,
        icon_path=resource_path("icon.ico"),
        duration=5,
        threaded=True
    )

    menu = Menu(
        MenuItem('Switch Personality', toggle_personality),
        MenuItem('Quit', exit_app)
    )
    icon = Icon("virtual_roommate", image, "Virtual Roommate", menu)
    icon.run()


if __name__ == "__main__":
    try:
        setup_tray()
    except Exception as e:
        import traceback
        with open("error.log", "w") as f:
            f.write(traceback.format_exc())

# pyinstaller main.py --name "VirtualRoommate" --icon=icon.ico --noconsole