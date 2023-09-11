import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from moving_average import moving_average

#DATA
stock = pd.read_csv('AAPL.csv')
comparison = stock['Close'][8:]

#SMA
sma = moving_average(stock, 'simple', 8, 20)


if __name__ == '__main__':
    print(sma)
