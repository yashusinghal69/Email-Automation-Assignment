import requests
import json
import time
from typing import List, Dict

 

def send_telegram_message(bot_token, chat_id, message):
    """Send a single message via Telegram Bot API"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response.json()


def send_messages_to_telegram(messages, bot_token, chat_id, max_messages=None, delay=1):
    """Send multiple messages to a Telegram chat"""
    sent_count = 0
    
    for i, msg in enumerate(messages):
        if max_messages is not None and i >= max_messages:
            print(f"⏩ Skipped remaining {len(messages) - i} messages (reached limit)")
            break
        
        email = msg.get('email', '')
        content = msg.get('email_message', '')
        first_name = msg.get('first_name', 'there')
        
        # Format message for Telegram (with HTML formatting)
        telegram_msg = f"<b>To:</b> {email}\n"
        telegram_msg += f"<b>Subject:</b> AI Workshop Follow-up for {first_name}\n\n"
        telegram_msg += content.replace('\n', '\n')
        
        # Send to Telegram
        result = send_telegram_message(bot_token, chat_id, telegram_msg)
        if result.get('ok'):
            print(f"✅ Message sent to Telegram for {email}")
            sent_count += 1
        else:
            print(f"❌ Failed to send message for {email}: {result.get('description')}")
        
        # Delay to avoid rate limiting
        time.sleep(delay)
    
    print(f"\n{'='*50}")
    print(f"📊 TELEGRAM SENDING SUMMARY")
    print(f"{'='*50}")
    print(f"✅ Messages sent: {sent_count}")
    print(f"{'='*50}")
    
    return sent_count

def main():
    # Configuration for Telegram
    bot_token = "<YOUR_BOT_TOKEN_HERE>"
    chat_id = "<YOUR_CHAT_ID_HERE>"
    
    #read this article to get your bot token and chat id: https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a


    # Load messages
    with open("message_generation/personalized_messages.json", 'r', encoding='utf-8') as f:
        messages = json.load(f)
    
    print(f"✅ Loaded {len(messages)} messages from personalized_messages.json")
    
    # Send to Telegram
    send_messages_to_telegram(
        messages[:10],  # Send only the first 10 messages
        bot_token,
        chat_id,
        max_messages=10,  # Limit number of messages
        delay=1.5         # Delay between messages (seconds)
    )

if __name__ == "__main__":
    main()
