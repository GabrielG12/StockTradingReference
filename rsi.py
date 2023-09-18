import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
