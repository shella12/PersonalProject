from twilio.rest import Client
import os
from dotenv import load_dotenv
# Fill in your credentials and numbers

load_dotenv()
TWILIO_SID = os.getenv("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("ACCOUNT_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox number
YOUR_WHATSAPP_NUMBER = os.getenv("PHONE_NUMBER")    # Your verified number

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp(message):
    try:
        msg = client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=YOUR_WHATSAPP_NUMBER
        )
        print(f"[+] WhatsApp sent: {msg.sid}")
    except Exception as e:
        print("[-] WhatsApp send failed:", e)
