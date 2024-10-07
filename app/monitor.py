import logging
import requests
import time
from app.config import APPLICATIONS, DEFAULT_WEBHOOK_URL, CHECK_INTERVAL

def send_discord_notification(webhook_url, message):
    data = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code != 204:
            logging.error(f"Failed to send Discord notification: {response.text}")
    except Exception as e:
        logging.error(f"Failed to send Discord notification: {str(e)}", exc_info=True)

def check_health(application):
    try:
        response = requests.get(application['url'])
        if response.status_code != 200:
            send_discord_notification(
                application.get("webhook_url", DEFAULT_WEBHOOK_URL), 
                f"🚨 **{application['name']}** is unhealthy:\n"
                f"**Status Code:** {response.status_code}\n"
                f"**URL:** {application['url']}\n"
                f"**Response Time:** {response.elapsed.total_seconds()} seconds\n"
                f"**Response Content:** {response.text[:300]}...\n"
            )
    except requests.exceptions.RequestException as e:
        send_discord_notification(application.get("webhook_url", DEFAULT_WEBHOOK_URL), f"🚨 {application['name']} health check failed: {str(e)}")

def main():
    while True:
        for app in APPLICATIONS:
            check_health(app)
        time.sleep(CHECK_INTERVAL)  # Sleep interval in seconds
