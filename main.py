import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from moving_average import calculate_sma, calculate_ema
from stock_scrapping import get_stock
from rsi import calculate_rsi

#SMA
stock_name = 'NVDA'
stock = get_stock(stock_name, 'US5L2Y3PKRB2AVQO', 'daily', 150)
sma = calculate_sma(stock, 8, 50)
ema = calculate_ema(stock, 8, 50)
rsi = calculate_rsi(stock, 14)

if __name__ == '__main__':
    print(f"The RSI of {stock_name} is {rsi}")
