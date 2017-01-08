import keyboard
import datetime
from send_clipboard_keys import main

last_time_pressed = datetime.datetime.now()


def handle_hotkey():
    global last_time_pressed
    now = datetime.datetime.now()
    delta = now - last_time_pressed
    if delta.total_seconds() > 3:
        main()
        last_time_pressed = now


hotkey = keyboard.add_hotkey(
    'ctrl+alt+shift+k,Home', handle_hotkey, blocking=True, timeout=3)
recorded = keyboard.record(until='esc')
