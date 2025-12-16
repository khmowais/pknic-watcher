#PKNIC domain watcher bot

This Python script checks the availability of domains on [PKNIC](https://www.pknic.net.pk/) and sends notifications via **Telegram** and **Email** when domain status changes.

---

### Edit `pknic_config.py`

Fill in your credentials:

```python
DOMAINS = ["owais.pk"]

ENABLE_TELEGRAM = True
ENABLE_EMAIL = True

# Telegram Bot Configuration
TG_BOT_TOKEN = "PUT_BOT_TOKEN_HERE"
TG_CHAT_ID = "PUT_CHAT_ID_HERE"

# Gmail SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"
SMTP_PASS = "PUT_APP_PASSWORD_HERE"
EMAIL_TO = "your_email@gmail.com"
```

---

## How to get your secrets

### 1. Gmail app password

1. Enable **2-Step Verification**: [Google 2FA Setup](https://myaccount.google.com/security)
2. Create an **App Password** for this script: [Google App Passwords](https://myaccount.google.com/apppasswords)

   * Select **Other (Custom name)** → Name it `"PKNIC Bot"`
   * Copy the 16-character App Password and use it as `SMTP_PASS`.

### 2. Telegram Bot Token

1. Open Telegram and search **@BotFather**.
2. Send `/newbot` and follow instructions.
3. Copy the **Bot Token** given by BotFather.
4. Send a message to your bot to get your **Chat ID**:

   * You can use the API:

     ```
     https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
     ```
   * Look for `"chat":{"id":YOUR_CHAT_ID}` in the JSON response.

---

## Automate with Cron

Check the domain periodically by adding a cron job:

```bash
crontab -e
```

For example to run every 30 minutes:

```
*/30 * * * * /usr/bin/python3 /home/YOUR_USERNAME/path/to/pknic_watch.py
```

---

## Notes
* Add more domains in the `DOMAINS` list if needed.
* The script stores last-known domain states locally in `STATE_DIR` (`~/pknic_state` by default).
