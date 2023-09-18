import numpy as np


def calculate_rsi(data, window=14):
    close_prices = np.array(data)
    delta = np.diff(close_prices)

    gains = np.where(delta > 0, delta, 0)
    losses = np.where(delta < 0, -delta, 0)

    avg_gain = np.mean(gains[:window])
    avg_loss = np.mean(losses[:window])

    rs = avg_gain / avg_loss if avg_loss != 0 else np.inf
    rsi = 100 - (100 / (1 + rs))

    return rsi


# Example data (closing prices)
closing_prices = [50, 51, 52, 48, 49, 47, 45, 46, 47, 48, 50, 51, 52, 50]

# Calculate RSI with a window of 14 periods
rsi = calculate_rsi(closing_prices, window=14)

print("RSI:", rsi)
