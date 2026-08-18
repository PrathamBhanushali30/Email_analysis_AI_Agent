import time, json, os
from gmail_fetcher import fetch_unread_emails
from main_agent import analyze_email
from alert import send_alert

LOG_FILE = "logs.json"

def save_log(entry):
    data = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)


def main():
    print("Running AI Email Security System...")

    while True:
        emails = fetch_unread_emails()

        for e in emails:
            result = analyze_email(e)
            save_log(result)

            if "MALICIOUS" in result["final"] or "SUSPICIOUS" in result["final"]:
                send_alert(result["final"])

        time.sleep(60)


if __name__ == "__main__":
    main()