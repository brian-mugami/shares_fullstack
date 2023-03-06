from dotenv import load_dotenv
import requests
import os

load_dotenv()

DOMAIN_NAME = os.getenv("API_DOMAIN")
API_KEY = os.getenv("API_KEY")

def send_email(recipient, text, subject):
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", API_KEY),
        data={"from": "Shares Admin <kindredsolutions254@gmail.com>",
              "to": [recipient,],
              "subject": subject,
              "text": text}
    )