# PKNIC Domain Watcher Bot

This Python script allows you to monitor the availability of domains on [PKNIC](https://www.pknic.net.pk/) and receive notifications via **Telegram** and **Email** whenever the status of your domains changes.

---

## How to Use:

### 1. Clone repository

Clone this repository to your machine:

```bash
git clone https://github.com/YOUR_USERNAME/pknic-watcher.git
cd pknic-watcher
```

### 2. Edit `pknic_config.py`

Fill in your credentials in the `pknic_config.py` file:

```python
DOMAINS = ["some_pk_domain.pk"]  # Add domains you want to check

ENABLE_TELEGRAM = True  # Enable/Disable Telegram notifications
ENABLE_EMAIL = True  # Enable/Disable email notifications

# Telegram Bot Configuration
TG_BOT_TOKEN = "PUT_BOT_TOKEN_HERE"
TG_CHAT_ID = "PUT_CHAT_ID_HERE"

# Gmail SMTP Configuration (for email notifications)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"  # Your email address for the App Password
SMTP_PASS = "PUT_APP_PASSWORD_HERE"  # Use the App Password generated below
EMAIL_TO = "your_email@gmail.com"  # Email address to receive notifications
```

---

## How to get your Token/Password

### 1. **Gmail App Password**

To send emails from your gmail account, you need to create an **App Password**.

1. Enable **2-Step Verification** on your Google account: [Google 2FA Setup](https://myaccount.google.com/security)
2. Generate an **App Password**: [Google App Passwords](https://myaccount.google.com/apppasswords)

   * Select **Other (Custom name)** and name it `"PKNIC Bot"`.
   * Copy the generated 16-character password and use it as `SMTP_PASS` in your config.

### 2. **Telegram Bot Token**

To enable Telegram notifications, follow these steps:

1. Open Telegram and search for **@BotFather**.
2. Send `/newbot` and follow the instructions to create your bot.
3. Copy the **Bot Token** given by **BotFather**.
4. To get your **Chat ID**, send a message to your bot and use the following URL to find it:

   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```

   * Look for `"chat": {"id": YOUR_CHAT_ID}` in the JSON response.

---

## Automate with Cron

To run the script periodically, add a cron job:

1. Open your crontab configuration:

   ```bash
   crontab -e
   ```

2. Add the following line to run the script every 30 minutes (adjust the path to your script):

   ```
   */30 * * * * /usr/bin/python3 /home/YOUR_USERNAME/path/to/pknic_watch.py
   ```


## Storage of domain states

The script saves the last known domain status locally in `STATE_DIR`. This helps in detecting changes in domain status over time.


## Troubleshooting

* If the script is not working as expected, check for errors in the terminal and ensure that you’ve filled in all fields in config properly.
* **Test the email** and **Telegram** configurations separately to ensure both work before running the full script.
* I would suggest to delete all txt files in `STATE_DIR` and then running script atleast once so you can test the notifications being received.