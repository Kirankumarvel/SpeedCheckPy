# ⚡ SpeedCheckPy

A lightweight Python tool to check your internet connection speed — including **download**, **upload**, and **ping** — using the `speedtest-cli` library.

---

## 📌 Features

- 📥 Measure **Download Speed** (in Mbps)
- 📤 Measure **Upload Speed** (in Mbps)
- 🛰️ Get current **Ping** (latency in ms)
- 💻 Simple and beginner-friendly script
- 🐍 Fully written in Python – no browser required

---

## 🛠️ Requirements

- Python 3.x
- `speedtest-cli` Python library

### 📦 Install Requirements

```bash
pip install speedtest-cli


---

🚀 How to Run

1. Clone or download this repo:



git clone https://github.com/yourusername/SpeedCheckPy.git
cd SpeedCheckPy

2. Run the script:



python speed_check.py


---

📄 Example Output

Download Speed in Mbps: 87.32
Upload Speed in Mbps: 56.21
Ping: 23.65


---

📁 Project Structure

SpeedCheckPy/
├── speed_check.py          # Main script to test internet speed
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies


---

📜 Code Overview

import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    down_speed = round(test.download() / 10**6, 2)
    print("Download Speed in Mbps:", down_speed)

    up_speed = round(test.upload() / 10**6, 2)
    print("Upload Speed in Mbps:", up_speed)

    ping = test.results.ping
    print("Ping:", ping)

Speed_Test()


---

🧠 Why Use This?

Whether you're troubleshooting a slow connection or need a quick CLI-based alternative to browser tools like speedtest.net, this script offers a fast, minimal, and Pythonic way to test your network performance.


---

🔧 To-Do / Ideas

[ ] GUI version using Tkinter or PyQt

[ ] Logging results to a file

[ ] Scheduled checks for continuous monitoring



---

🙌 Credits

Built with speedtest-cli by @sivel

Developed as part of Python Interview Practice Lab



---

📃 License

This project is licensed under the MIT License.
