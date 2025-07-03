# Trading Alert Bot
**Automated Bollinger Band Alerts for Crypto Trading**

---

## Project Overview

This Python bot monitors cryptocurrency prices (e.g., BTCUSDT) on Binance in real time. It checks if the price breaches the upper or lower Bollinger Band. When a breach is detected, it instantly sends a WhatsApp alert using Twilio, so you never miss a trading opportunity.

---

## Features

- **Real-time Monitoring:** Continuously checks the latest price of BTCUSDT from Binance.
- **Bollinger Bands Calculation:** Automatically computes upper and lower Bollinger Bands based on recent price data.
- **Automated Alerts:** Sends instant WhatsApp notifications via Twilio when price breaches bands (above upper or below lower).
- **Customizable:** Easily change symbol, timeframe, or Bollinger Band settings.

---

## Tech Stack

- **Python 3**
- **Binance API** (price data)
- **Pandas, NumPy** (data analysis)
- **Twilio API** (WhatsApp messaging)

---

## How It Works

1. **Fetches Price Data:** Uses Binance API to get the latest BTCUSDT price and historical data.
2. **Calculates Bollinger Bands:** Computes moving average and bands.
3. **Compares Price:** Checks if the latest price crosses above or below the bands.
4. **Sends Alert:** If breached, sends a WhatsApp message using Twilio.

---

## Sample Alert

> “BTCUSDT Alert: Price breached upper Bollinger Band! Current Price: $xxxxx”

---

## Screenshots

*Include a screenshot or sample of the WhatsApp message if you have it!*

---

## Getting Started

### Prerequisites

- Python 3.x installed
- Twilio account & WhatsApp sandbox setup
- Binance API keys (optional for advanced usage)

### Installation

```bash
git clone https://github.com/shella12/PersonalProject.git
cd PersonalProject
pip install -r requirements.txt
