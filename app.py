import keyboard
import datetime
from send_keys_from_image import main, send_keys

last_time_pressed = datetime.datetime.now()


def handle_send_keys_hotkey():
    keyboard.remove_hotkey(send_keys_hotkey)
    send_keys()


def handle_hotkey():
    global last_time_pressed, send_keys_hotkey
    now = datetime.datetime.now()
    delta = now - last_time_pressed
    if delta.total_seconds() > 3:
        last_time_pressed = now
        is_success = main()
        if is_success:
            send_keys_hotkey = keyboard.add_hotkey(
                'Home', handle_send_keys_hotkey)


capture_and_render_image_to_text_hotkey = keyboard.add_hotkey(
    'ctrl+alt+shift+k,Home', handle_hotkey, blocking=True, timeout=3)


recorded = keyboard.record(until='esc')
