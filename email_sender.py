import smtplib
import ssl
import time
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def setup_smtp(smtp_server, port, sender_email, password):
    """Create and return an SMTP server connection"""
    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)
    return server

def send_email(server, sender_email, recipient_email, subject, content):
    """Send a single email with the given content"""
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email
    
    # Plain text version
    text_part = MIMEText(content, "plain")
    message.attach(text_part)
    
    # Simple HTML version
    html_content = f"<html><body><p>{content.replace('\n\n', '</p><p>').replace('\n', '<br>')}</p></body></html>"
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)
    
    server.sendmail(sender_email, recipient_email, message.as_string())
    print(f"✅ Email sent to {recipient_email}")



def send_bulk_emails_from_json(smtp_server, port, sender_email, password, json_file, test_mode=True, max_emails=5, delay=2):

    # Load messages from JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    print(f"✅ Loaded {len(messages)} messages from {json_file}")
    
    sent_count = 0
    
    if test_mode:
        print("🔬 TEST MODE - Emails will not be actually sent")
        if max_emails is None:
            max_emails = 2
    
    # Connect to SMTP server if not in test mode
    if not test_mode:
        server = setup_smtp(smtp_server, port, sender_email, password)
    
    # Process each message
    for i, msg in enumerate(messages):
        if max_emails is not None and i >= max_emails:
            print(f"⏩ Skipped remaining {len(messages) - i} emails (reached limit)")
            break
        
        email = msg.get('email', '')
        message = msg.get('email_message', '')
        
        # Skip if no valid email
        if not email or '@' not in email:
            continue
            
        # Create a subject (using first name if available)
        first_name = msg.get('first_name', 'there')
        subject = f"AI Workshop Follow-up for {first_name}"
        
        if test_mode:
            print(f"📧 Would send to: {email}")
            print(f"📑 Subject: {subject}")
            print(f"💬 Preview: {message[:100]}...")
            time.sleep(0.5)
        else:
            send_email(server, sender_email, email, subject, message)
            time.sleep(delay)
            
        sent_count += 1
    
    print(f"\n{'='*50}")
    print(f"📊 EMAIL SENDING SUMMARY")
    print(f"{'='*50}")
    print(f"✅ Emails processed: {sent_count}")
    print(f"{'='*50}")
    
    # Close connection if not in test mode
    if not test_mode:
        server.quit()




# If you don't see 2-step verification, you can enable it and then create an App Password for your email client.

# In https://myaccount.google.com/security, do you see 2-step verification set to ON? If yes, then visiting https://myaccount.google.com/apppasswords should allow you to set up application specific passwords. 


def main():
    # Email configuration
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "<your_email_address>"

    # Use an App Password instead of your regular password
    password = "<your_app_password>"

    # Or send emails from JSON
    send_bulk_emails_from_json(
        smtp_server, 
        port, 
        sender_email, 
        password, 
        'personalized_messages.json',
        test_mode=False,
        max_emails=5,
        delay=2
    )

if __name__ == "__main__":
    main()
