# AI Security Alert Analyzer
A Python-based security monitoring tool that analyzes authentication logs, detects suspicious activity, and generates concise AI-powered insights.


## 🚀 Features
* Parses login logs (failed, invalid, successful attempts)
* Assigns severity levels: LOW, MEDIUM, HIGH, CRITICAL
* Clean structured output (timestamp → IP → attempts → level → analysis)
* Color-coded and bold severity indicators (Tkinter UI)
* Short AI-generated analysis (max 3 lines for fast decision-making)


## 🧠 Why this project?
Security analysts don’t have time to read long logs.

This tool transforms raw log data into:

* Structured alerts
* Clear severity levels
* Quick AI-based explanations

Inspired by SIEM tools, but enhanced with AI for faster understanding.


## 🛠 Tech Stack
* Python
* Tkinter (UI)
* Requests (API calls)
* Ollama (Local LLM)

## ⚙️ How it works
1. Reads log file (`log.txt`)
2. Extracts login activity per IP
3. Calculates severity level
4. Displays structured alerts in UI
5. Generates short AI analysis for high-risk alerts

## 📸 Example Output

<img width="811" height="492" alt="Screenshot 2026-04-24 153054" src="https://github.com/user-attachments/assets/f5ac6dbc-52cd-43fc-afc9-444b24121ab3" />



## ▶️ Setup & Run

Install dependencies:
```
pip install requests
```
Make sure Ollama is running locally.

Run the project:
```
python main.py
```

## 📌 Project Highlights
* Built a mini SIEM-style alert analyzer
* Integrated local AI for security insights
* Focused on clarity and real-world usability


## 🔗 Future Improvements
* Real-time log monitoring
* Support for system logs (auth.log)
* Alert filtering and dashboard features
