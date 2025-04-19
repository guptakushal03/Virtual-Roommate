from pynput import mouse, keyboard
import time
import threading
from win10toast_click import ToastNotifier
import pyttsx3
import random

toaster = ToastNotifier()
last_activity_time = time.time()
afk_threshold = 600

GREMLIN_IDLE_QUOTES = [
    "Did you fall asleep at your desk?",
    "If you're not here, I'm watching memes in your place.",
    "MOVE! You're not a statue.",
]

ZEN_IDLE_QUOTES = [
    "Step away and return refreshed.",
    "A break is a breath for the mind.",
    "Stillness is okay — just don’t forget to return. 🧘"
]

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def on_activity(_):
    global last_activity_time
    last_activity_time = time.time()

def start_input_listener():
    mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity)
    keyboard_listener = keyboard.Listener(on_press=on_activity)

    mouse_listener.start()
    keyboard_listener.start()

def afk_monitor_loop(get_personality_fn):
    global last_activity_time
    while True:
        time.sleep(60) 
        idle_time = time.time() - last_activity_time
        if idle_time > afk_threshold:
            personality = get_personality_fn()
            quote = random.choice(ZEN_IDLE_QUOTES if personality == "zen" else GREMLIN_IDLE_QUOTES)
            toaster.show_toast(
                "Virtual Roommate",
                quote,
                icon_path="icon.ico",
                duration=10,
                threaded=True
            )
            speak(quote)
            last_activity_time = time.time()