#!/usr/bin/env python3

import requests
import smtplib
import os
from email.message import EmailMessage
from datetime import datetime

import pknic_config as cfg


LOOKUP_URL = "https://pk6.pknic.net.pk/pk5/lookup.PK"

STATE_DIR = "/home/ap2kmo/rndm_files/pknic_state" #directory to store domain status, change as needed


def send_telegram(message):
    if not cfg.ENABLE_TELEGRAM:
        return

]    requests.post(
        f"https://api.telegram.org/bot{cfg.TG_BOT_TOKEN}/sendMessage",
        data={"chat_id": cfg.TG_CHAT_ID, "text": message},
        timeout=10
    )


def send_email(subject, body):
    if not cfg.ENABLE_EMAIL:
        return

    msg = EmailMessage()
    msg["From"] = cfg.SMTP_USER
    msg["To"] = cfg.EMAIL_TO
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(cfg.SMTP_SERVER, cfg.SMTP_PORT) as s:
        s.starttls()
        s.login(cfg.SMTP_USER, cfg.SMTP_PASS)
        s.send_message(msg)


def detect_status(text):
    text = text.lower()

    if "domain not found" in text and "not registered" in text:
        return "AVAILABLE"

    if "domain is registered" in text:
        return "REGISTERED"

    return "UNKNOWN"


def notify(domain, old, new):
    message = (
        f"PKNIC DOMAIN STATUS CHANGED\n\n"
        f"Domain: {domain}\n"
        f"Old Status: {old}\n"
        f"New Status: {new}\n"
        f"Time: {datetime.now()}\n\n"
        f"https://www.pknic.net.pk/"
    )

    send_telegram(message)
    send_email(f"PKNIC Alert: {domain}", message)


def main():
    os.makedirs(STATE_DIR, exist_ok=True)

    for domain in cfg.DOMAINS:
        try:
            r = requests.post(
                LOOKUP_URL,
                data={"name": domain},
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=30
            )
            r.raise_for_status()

            status = detect_status(r.text)

            state_file = f"{STATE_DIR}/{domain}.txt"
            old_status = None

            if os.path.exists(state_file):
                with open(state_file) as f:
                    old_status = f.read().strip()

            if old_status != status:
                notify(domain, old_status, status)

            with open(state_file, "w") as f:
                f.write(status)

        except Exception as e:
            print(f"[ERROR] {domain}: {e}")


if __name__ == "__main__":
    main()