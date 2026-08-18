import smtplib, os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")

def send_alert(message):
    msg = MIMEText(message)
    msg["Subject"] = "Suspicious Email Detected"
    msg["From"] = EMAIL_USER
    msg["To"] = ALERT_EMAIL

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, ALERT_EMAIL, msg.as_string())
    server.quit()