#!/usr/bin/env python3
# ================= CONFIG =================


DOMAINS = [ #domains to check
    "some_domain.pk"
]

# ---- Notifications Toggle ----
ENABLE_TELEGRAM = True
ENABLE_EMAIL = True

# ---- Telegram ----
TG_BOT_TOKEN = "PUT_BOT_TOKEN_HERE"
TG_CHAT_ID = "PUT_CHAT_ID_HERE"

# ---- Email ----
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "sender@gmail.com"
SMTP_PASS = "aaaa bbbb cccc dddd"
EMAIL_TO = "receiver@gmail.com"
