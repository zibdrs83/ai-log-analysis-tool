import requests

def ai_explain(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    
    return response.json()["response"]


with open("log.txt", "r") as file:
    logs = file.readlines()

# store activity
ip_activity = {}

for line in logs:

    # FAILED LOGIN
    if "Failed password" in line:
        parts = line.split("from ")
        ip = parts[1].split(" ")[0]

        if ip not in ip_activity:
            ip_activity[ip] = {"failed": 0, "invalid": 0, "success": 0}

        ip_activity[ip]["failed"] += 1

        if "invalid user" in line:
            ip_activity[ip]["invalid"] += 1

    # SUCCESSFUL LOGIN
    if "Accepted password" in line:
        parts = line.split("from ")
        ip = parts[1].split(" ")[0]

        if ip not in ip_activity:
            ip_activity[ip] = {"failed": 0, "invalid": 0, "success": 0}

        ip_activity[ip]["success"] += 1

# OPEN REPORT FILE
report = open("report.txt", "w", encoding="utf-8")

print("\n==============================")
print("SECURITY ANALYSIS REPORT")
print("==============================\n")

report.write("==============================\n")
report.write("SECURITY ANALYSIS REPORT\n")
report.write("==============================\n\n")

# SECOND LOOP -> ANALYSIS + AI
priority = {
    "CRITICAL": 0,
    "HIGH": 1,
    "MEDIUM": 2,
    "LOW": 3
}


for ip, activity in sorted(
    ip_activity.items(),
    key=lambda item: priority[
        "CRITICAL" if item[1]["failed"] > 2 and item[1]["success"] > 0
        else "HIGH" if item[1]["failed"] > 5 or item[1]["invalid"] > 5
        else "MEDIUM" if item[1]["failed"] > 2 or item[1]["invalid"] > 2
        else "LOW"
    ]
):

    failed = activity["failed"]
    invalid = activity["invalid"]
    success = activity["success"]

    if failed > 2 and success > 0:
       level = "CRITICAL"
    elif failed > 5 or invalid > 5:
       level = "HIGH"
    elif failed > 2 or invalid > 2:
       level = "MEDIUM"
    else:
       level = "LOW"

    alert_line = f"IP: {ip}\nLevel: {level}\nFailed: {failed} | Invalid: {invalid} | Success: {success}"

    if level in ["CRITICAL", "HIGH", "MEDIUM"]:
        prompt = f"""
You are a cybersecurity analyst.

Analyze this login activity and explain it briefly in 2 lines.

IP: {ip}
Risk Level: {level}
Failed attempts: {failed}
Invalid usernames: {invalid}
Successful logins: {success}

Focus only on whether this looks suspicious, what kind of attack it may suggest, and why.
Do not explain what an IP address is.
Do not speak to the user directly.
"""
        explanation = ai_explain(prompt)
    else:
        explanation = "Skipped for low-risk activity."

    print("------------------------------")
    print(alert_line)
    print("AI Insight:")
    print(explanation)
    print("------------------------------\n")

    report.write("------------------------------\n")
    report.write(alert_line + "\n")
    report.write("AI Insight:\n")
    report.write(explanation + "\n")
    report.write("------------------------------\n\n")

report.close()