import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Usage check
if len(sys.argv) < 3: 
    print("Usage: send_email.py <recipient_email> <your_message>")
    sys.exit(1)

receiver_email = sys.argv[1]
your_message = sys.argv[2]

# Gmail credentials (replace these!)
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_16_digit_app_password"

# Email subject and body
subject = "Message from Terminal App"
body = f"{your_message}"

# Build email
message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect and send
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
    server.quit()

    print(f"✅ Message sent to {receiver_email}")
except Exception as e:
    print(f"Error: {e}")
