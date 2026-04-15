# 🔐 Anti-Keylogger Detection & Response System (Python)

## 📌 Overview

This project is a **demo cybersecurity tool** that simulates the detection and response to basic keylogger activity in real time. It monitors running processes to identify suspicious scripts (like `keylogger.py`), terminates them, and immediately alerts the user through a graphical dashboard.

Once a threat is detected, the system blocks keyboard input to prevent further data capture and provides multiple response options such as viewing the file location, quarantining the file, restoring it, or permanently deleting it. The tool also maintains an activity log for tracking actions and detected threats.

⚠️ **This project is strictly a demonstration and learning tool.** It showcases how basic keylogger detection and response *can be implemented*, but it is **not a real security solution** and should not be used for actual malware protection.

---

## 🚀 Features

* 🔍 Detects suspicious keylogger processes
* ❌ Terminates detected keylogger automatically
* 🔒 Blocks keyboard input upon detection
* 🖥️ GUI dashboard using Tkinter
* 📂 File actions: Open, Quarantine, Restore, Delete
* 📝 Activity logging system
* 🧪 Includes a simulated keylogger for testing

---

## ⚙️ Requirements

```
psutil
keyboard
pynput
cryptography
```

---

## 🧪 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Start the Anti-Keylogger

```bash
python main.py
```

### Step 2: Run the Keylogger (for testing)

```bash
python keylogger.py
```

---

## ⚠️ Important Notes

* This project is for **educational purposes only**
* This is a **demo implementation**, not real-world protection
* Detection is based on simple checks (e.g., filename `keylogger.py`)
* It will **NOT detect advanced or hidden keyloggers**
* `keyboard` module may require **administrator/root privileges**
* Works best on **Windows**

---

## 💡 Limitations

* Detection relies on **process command-line inspection**
* Can be bypassed easily (e.g., renaming the file)
* No behavioral or signature-based malware detection
* Not suitable for production use

---

## 📁 Project Structure

```
├── main.py              # Anti-keylogger detection system
├── keylogger.py         # Simulated keylogger for testing
├── activity_log.txt     # Logs system activity
├── quarantine/          # Stores quarantined files
├── requirements.txt
└── README.md
```

---

## 🛡️ Disclaimer

This project is intended for **learning and demonstration purposes only**. Do not use it for malicious activities or as a replacement for real cybersecurity tools.

---
