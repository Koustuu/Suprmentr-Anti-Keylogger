# -*- coding: utf-8 -*-

import os
import time
import threading
import shutil
import psutil
import tkinter as tk
import keyboard

# -----------------------------
# SETUP
# -----------------------------
activity_log = "activity_log.txt"

detected_file_path = None

quarantine_dir = "quarantine"
quarantined_file = None
original_path = None

triggered = False

# -----------------------------
# LOG FUNCTION
# -----------------------------
def log(msg):
    with open(activity_log, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} - {msg}\n")

# -----------------------------
# DETECT KEYLOGGER PROCESS
# -----------------------------
def detect_keylogger_process():
    global detected_file_path

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline_list = proc.info['cmdline']

            if cmdline_list:
                for part in cmdline_list:
                    if "keylogger.py" in part:
                        detected_file_path = os.path.abspath(part)
                        log(f"⚠️ Detected keylogger: {detected_file_path}")
                        return proc
        except:
            pass

    return None

# -----------------------------
# ALERT TRIGGER
# -----------------------------
def trigger_alert():
    block_keyboard()
    start_ui()

# -----------------------------
# KEYBOARD CONTROL
# -----------------------------
def block_keyboard():
    log("Keyboard blocked")
    for i in range(150):
        try:
            keyboard.block_key(i)
        except:
            pass

def unblock_keyboard():
    keyboard.unhook_all()
    log("Keyboard unblocked")
    status_label.config(text="🟢 Keyboard Unblocked", fg="#00ff9f")

# -----------------------------
# ACTIONS
# -----------------------------
def open_location():
    if detected_file_path:
        os.startfile(os.path.dirname(detected_file_path))
        log("Opened keylogger location")

def contain_file():
    global quarantined_file, original_path

    log("Contain selected")

    try:
        os.makedirs(quarantine_dir, exist_ok=True)

        original_path = detected_file_path
        quarantined_file = os.path.join(quarantine_dir, os.path.basename(detected_file_path))

        shutil.move(detected_file_path, quarantined_file)

        status_label.config(text="🟡 File Quarantined", fg="yellow")
        log("File moved to quarantine")

    except Exception as e:
        log(f"Contain failed: {e}")

def restore_file():
    global quarantined_file, original_path

    log("Restore selected")

    try:
        if quarantined_file and os.path.exists(quarantined_file):
            shutil.move(quarantined_file, original_path)
            status_label.config(text="🟢 File Restored", fg="#00ff9f")
            log("File restored")
        else:
            status_label.config(text="⚠️ No file found", fg="orange")

    except Exception as e:
        log(f"Restore failed: {e}")

def delete_file():
    log("Delete selected")

    try:
        if quarantined_file and os.path.exists(quarantined_file):
            os.remove(quarantined_file)
        elif detected_file_path and os.path.exists(detected_file_path):
            os.remove(detected_file_path)

        status_label.config(text="🔴 File Deleted", fg="red")
        log("File deleted")

    except Exception as e:
        log(f"Delete failed: {e}")

# -----------------------------
# UI DASHBOARD
# -----------------------------
def start_ui():
    global status_label

    root = tk.Tk()
    root.title("Anti-Keylogger Dashboard")
    root.geometry("500x350")
    root.configure(bg="#0f172a")

    def style_button(btn):
        btn.configure(
            bg="#1e293b",
            fg="white",
            activebackground="#334155",
            relief="flat",
            width=15
        )

    tk.Label(root, text="⚠️ KEYLOGGER DETECTED",
             font=("Arial", 16, "bold"),
             fg="#ff4d4d", bg="#0f172a").pack(pady=15)

    status_label = tk.Label(root, text="🔒 Keyboard Blocked",
                            fg="#ffaa00", bg="#0f172a")
    status_label.pack()

    tk.Label(root, text="Suspicious File:",
             fg="white", bg="#0f172a").pack()

    tk.Label(root, text=detected_file_path,
             fg="#38bdf8", bg="#0f172a", wraplength=400).pack(pady=5)

    frame = tk.Frame(root, bg="#0f172a")
    frame.pack(pady=20)

    btn1 = tk.Button(frame, text="Open Location", command=open_location)
    btn2 = tk.Button(frame, text="Delete", command=delete_file)
    btn3 = tk.Button(frame, text="Contain", command=contain_file)
    btn4 = tk.Button(frame, text="Restore", command=restore_file)

    for b in [btn1, btn2, btn3, btn4]:
        style_button(b)

    btn1.grid(row=0, column=0, padx=5)
    btn2.grid(row=0, column=1, padx=5)
    btn3.grid(row=0, column=2, padx=5)
    btn4.grid(row=1, column=1, pady=10)

    tk.Button(root, text="Unblock Keyboard",
              command=unblock_keyboard,
              bg="#22c55e", fg="black").pack(pady=10)

    root.mainloop()

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print(" System monitoring started...")
    print(" Run keylogger.py to simulate attack")

    while True:
        proc = detect_keylogger_process()

        if proc and not triggered:
            triggered = True
            log(" Keylogger detected via process monitoring")

            try:
                proc.kill()
                log(" Keylogger process terminated")
            except:
                log("Failed to terminate process")

            trigger_alert()

        time.sleep(2)