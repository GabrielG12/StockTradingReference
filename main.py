import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from moving_average import calculate_sma, calculate_ema
from stock_scrapping import get_stock
from relative_strength_index import calculate_rsi

#TODO: SIMPLE/EXPONENTIAL MOVING AVERAGE
stock_name = 'NVDA'
stock = get_stock(stock_name, 'US5L2Y3PKRB2AVQO', 'daily', 150)
sma = calculate_sma(stock, moving_window_short=8, comparison=None, moving_window_long=None, show=None)
ema = calculate_ema(stock, period_short=8, comparison='yes', period_long=50, show=None)

#TODO: RELATIVE STRENGTH INDEX
rsi = calculate_rsi(stock, 14)
#print(f"The RSI of {stock_name} is {rsi}")

#TODO: MOVING AVERAGE CONVERGENCE/DIVERGENCE
_12_day_sma = calculate_sma(stock, moving_window_short=12)
_26_day_sma = calculate_sma(stock, moving_window_short=26)


if __name__ == '__main__':
    print()
