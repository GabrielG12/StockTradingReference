import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def moving_average(data: pd.DataFrame, average_type: str, moving_window_short: int, moving_window_long: int):

    #TODO: DATA PREPARATION
    price_data = data['Close']
    date_data = data['Date']

    last_window_index_short = len(price_data) - moving_window_short
    avg_window_series_short = []

    last_window_index_long = len(price_data) - moving_window_long
    avg_window_series_long = []

    #TODO: MOVING AVERAGE WINDOWS
    if average_type == 'simple':

        for i in range(0, last_window_index_short + 1):
            window_short = price_data[i:i+moving_window_short]
            avg_window_short = np.average(window_short)
            avg_window_series_short.append(avg_window_short)

        for j in range(0, last_window_index_long + 1):
            window_long = price_data[j:j+moving_window_long]
            avg_window_long = np.average(window_long)
            avg_window_series_long.append(avg_window_long)

        if len(avg_window_series_short) > len(avg_window_series_long):
            avg_window_series_short = avg_window_series_short[-len(avg_window_series_long):]

        #TODO: TRADING STRATEGIES

        #TODO: PLOTTING SMA
        y_label_average_short = avg_window_series_short
        y_label_average_long = avg_window_series_long
        y_label_original = price_data[-len(y_label_average_short):]
        x_label = list(range(0, len(avg_window_series_short)))
        plt.plot(x_label, y_label_average_short, 'r--', label='Simple Moving Average Short')
        plt.plot(x_label, y_label_average_long, 'b--', label='Simple Moving Average Long')
        plt.plot(x_label, y_label_original, 'g--', label='Original Price')
        plt.legend()
        plt.show()

    elif average_type == 'exponential':
        pass

    return
