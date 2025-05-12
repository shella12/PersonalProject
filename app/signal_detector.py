def detect_bollinger_signal(df):
    if df.empty:
        print("[!] DataFrame is empty. Skipping signal detection.", flush=True)
        return None

    df['MA20'] = df['close'].rolling(window=20).mean()
    df['STD20'] = df['close'].rolling(window=20).std()
    df['Upper'] = df['MA20'] + 2 * df['STD20']
    df['Lower'] = df['MA20'] - 2 * df['STD20']

    last = df.iloc[-1]
    print(f"Last close = {last['close']}", flush=True)
    print(f"Last Lower = {last['Lower']}", flush=True)
    print(f"Last Upper = {last['Upper']}", flush=True)

    if last['close'] > last['Upper']:
        return f"TRADE LOWER last price close: {last['Upper']}"
    elif last['close'] < last['Lower']:
        return f"TRADE HIGHER last price close: {last['Lower']}"
    return None
