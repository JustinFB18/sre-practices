import time
import requests
import logging
import os
from datetime import datetime
from smtplib import SMTP
from email.mime.text import MIMEText

# Configurations
URL = os.getenv("WEBSITE_MONITORING")  # Website to monitor
ALERT_THRESHOLD = 500  # Response time threshold in ms
SMTP_SERVER = "smtp.gmail.com"  # SMTP server for email alerts
SMTP_PORT = 587
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER_GROUP")

# Set up logging
logging.basicConfig(
    filename="website_monitor.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def send_alert(subject, message):
    """Send an alert email."""
    try:
        with SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            msg = MIMEText(message)
            msg["Subject"] = subject
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER
            smtp.send_message(msg)
            logging.info(f"Alert sent: {subject}")
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")

def check_website():
    """Check the website's availability and response time."""
    try:
        start_time = time.time()
        response = requests.get(URL)
        response_time = (time.time() - start_time) * 1000  # Convert to ms

        # Log metrics
        logging.info(f"URL: {URL}, Status: {response.status_code}, Response Time: {response_time:.2f}ms")

        # Check if alert is needed
        if response.status_code != 200:
            send_alert(
                "Website Down Alert",
                f"Website {URL} is down. Status Code: {response.status_code}",
            )
        elif response_time > ALERT_THRESHOLD:
            send_alert(
                "Slow Website Alert",
                f"Website {URL} is slow. Response Time: {response_time:.2f}ms",
            )
    except Exception as e:
        logging.error(f"Error checking website: {e}")
        send_alert("Website Monitor Error", f"An error occurred: {e}")

def main():
    """Main function to run the monitor."""
    logging.info("Starting website monitor...")
    check_website()

if __name__ == "__main__":
    main()
