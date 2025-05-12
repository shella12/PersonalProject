from app.data_fetcher import fetch_5m_candles
from app.signal_detector import detect_bollinger_signal
from app.notifier import send_whatsapp
import time
from datetime import datetime

def wait_until_next_5m():
    now = datetime.utcnow()
    seconds = (5 - now.minute % 5) * 60 - now.second
    print(f"[~] Waiting {seconds}s until next 5m candle close...")
    time.sleep(seconds)

def main():
    print("[*] Starting Bollinger Band 5m candle monitor...")

    while True:
        wait_until_next_5m()

        print("[+] Fetching 5m candle data...")
        df_5m = fetch_5m_candles()
        signal = detect_bollinger_signal(df_5m)

        if signal:
            message = f"🚨 {signal.upper()} SIGNAL - 5m candle breached Bollinger Band.\nTrade BTCUSDT for 10m interval."
            print("[!] Signal detected:", message)
            send_whatsapp(message)
        else:
            print("[-] No signal this candle.")

        # Wait just a bit before next fetch to avoid overlap
        time.sleep(5)

if __name__ == "__main__":
    main()
