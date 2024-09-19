import requests
import time
from app.config import APPLICATIONS, DISCORD_WEBHOOK_URL, CHECK_INTERVAL

def send_discord_notification(message):
    data = {
        "content": message
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code != 204:
            print(f"Failed to send notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending notification: {e}")

def check_health(application):
    try:
        response = requests.get(application['url'])
        if response.status_code != 200:
            send_discord_notification(f"🚨 {application['name']} is unhealthy: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        send_discord_notification(f"🚨 {application['name']} health check failed: {str(e)}")

def main():
    while True:
        for app in APPLICATIONS:
            check_health(app)
        time.sleep(CHECK_INTERVAL)  # Sleep interval in seconds
