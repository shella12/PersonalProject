from twilio.rest import Client

# Fill in your credentials and numbers
TWILIO_SID = "AC4d378599c13ba7fcb8185cde83b9ac75"
TWILIO_AUTH_TOKEN = "caa55e02754d5d2e1d2964f96c052817"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox number
YOUR_WHATSAPP_NUMBER = "whatsapp:+923325947980"    # Your verified number

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
