# AI Workshop Personalized Messaging System

A simple tool to generate and send personalized follow-up messages to AI workshop participants based on their job titles and attendance status.

## Features

- Categorizes recipients by job titles (student, developer, data scientist, etc.)
- Generates personalized email content based on job category and attendance
- Creates LinkedIn messages matched to recipient profiles
- Sends emails via SMTP (Gmail)
- Sends messages via Telegram
- Provides detailed statistics about message generation

## Setup

1. Install required packages:

   ```
   pip install -r requirements.txt
   ```

2. Place your participant data in CSV format with columns:

   - `first_name`
   - `email`
   - `Job Title`
   - `has_joined_event` (boolean)
   - `missing_linkedin` (boolean)

3. Configure email sending:

   - Create an App Password for Gmail: https://myaccount.google.com/apppasswords
   - Update `email_sender.py` with your email address and app password

4. For Telegram (optional):
   - Create a Telegram bot via BotFather and get the token
   - Get your chat ID
   - Update `telegram_sender.py` with your bot token and chat ID

## Usage

1. Generate personalized messages:

   ```
   python personalized_messaging.py
   ```

2. Send via email:

   ```
   python email_sender.py
   ```

3. Send via Telegram:
   ```
   python telegram_sender.py
   ```

## Files

- `personalized_messaging.py` - Core message generation
- `email_sender.py` - Email delivery via SMTP
- `telegram_sender.py` - Message delivery via Telegram

## Output

The system generates:

- `personalized_messages.csv` - Tabular format of all messages
- `personalized_messages.json` - Structured data with all message details
