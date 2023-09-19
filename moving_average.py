import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# TODO: SIMPLE MOVING AVERAGE
def calculate_sma(stock_data, moving_window_short: int, comparison=None,  show=None, moving_window_long=None):

    # DATA PREPARATION
    price_data = stock_data

    last_window_index_short = len(price_data) - moving_window_short
    avg_window_series_short = []

    # SMA SHORT WINDOW
    for i in range(0, last_window_index_short + 1):
        window_short = price_data[i:i + moving_window_short]
        avg_window_short = np.average(window_short)
        avg_window_series_short.append(avg_window_short)

    if comparison == 'yes' and moving_window_long is not None:

        last_window_index_long = len(price_data) - moving_window_long
        avg_window_series_long = []

        # SMA LONG WINDOW
        for j in range(0, last_window_index_long + 1):
            window_long = price_data[j:j + moving_window_long]
            avg_window_long = np.average(window_long)
            avg_window_series_long.append(avg_window_long)

        if len(avg_window_series_short) > len(avg_window_series_long):
            avg_window_series_short = avg_window_series_short[-len(avg_window_series_long):]

        if show == 'yes':

            # PLOTTING SMA COMPARISON
            y_label_average_short = avg_window_series_short
            y_label_average_long = avg_window_series_long
            y_label_original = price_data[-len(y_label_average_short):]
            x_label = list(range(0, len(avg_window_series_short)))
            plt.plot(x_label, y_label_original, 'g--', label='Original Price')
            plt.plot(x_label, y_label_average_short, 'r--', label=f'Simple Moving Average {moving_window_short} days')
            plt.plot(x_label, y_label_average_long, 'b--', label=f'Simple Moving Average {moving_window_long} days')
            plt.legend()
            plt.show()

        else:
            return avg_window_series_short, avg_window_series_long

    else:
        if show == 'yes':
            y_label_average_short = avg_window_series_short
            y_label_original = price_data[-len(y_label_average_short):]
            x_label = list(range(0, len(avg_window_series_short)))
            plt.plot(x_label, y_label_original, 'g--', label='Original Price')
            plt.plot(x_label, y_label_average_short, 'r--', label=f'Simple Moving Average {moving_window_short} days')
            plt.legend()
            plt.show()

        else:
            return avg_window_series_short


# TODO: EXPONENTIAL MOVING AVERAGE
def calculate_ema(stock_data, period_short: int, period_long=None, show=None, comparison=None):
    # DATA PREPARATION
    price_data = stock_data

    sma_window_short = price_data[0:period_short]
    ema_window_short = price_data[period_short:]
    ema_short = [np.average(sma_window_short)]
    alpha_short = 2 / (1 + period_short)

    # EMA SHORT WINDOW
    for i in range(len(ema_window_short)):
        ema_today_short = ((ema_window_short[i] - ema_short[-1]) * alpha_short) + ema_short[-1]
        ema_short.append(ema_today_short)

    if comparison == 'yes':

        sma_window_long = price_data[0:period_long]
        ema_window_long = price_data[period_long:]
        ema_long = [np.average(sma_window_long)]
        alpha_long = 2 / (1 + period_long)

        # EMA LONG WINDOW
        for j in range(len(ema_window_long)):
            ema_today_long = ((ema_window_long[j] - ema_long[-1]) * alpha_long) + ema_long[-1]
            ema_long.append(ema_today_long)

        if show == 'yes':
            # PLOTTING EMA
            y_label_original = price_data[-len(ema_long):]
            y_label_ema_short = ema_short[-len(ema_long):]
            y_label_ema_long = ema_long[:]
            x_label = list(range(0, len(ema_long)))
            plt.plot(x_label, y_label_original, 'g--', label='Original Price')
            plt.plot(x_label, y_label_ema_short, 'r--', label=f'Exponential Moving Average {period_short} days')
            plt.plot(x_label, y_label_ema_long, 'b--', label=f'Exponential Moving Average {period_long} days')
            plt.legend()
            plt.show()
        else:
            return ema_short[-len(ema_long):], ema_long[:]

    else:
        if show == 'yes':
            y_label_original = price_data[-len(ema_short):]
            y_label_ema_short = ema_short
            x_label = list(range(0, len(ema_short)))
            plt.plot(x_label, y_label_original, 'g--', label='Original Price')
            plt.plot(x_label, y_label_ema_short, 'r--', label=f'Exponential Moving Average {period_short} days')
            plt.legend()
            plt.show()
        else:
            return ema_short

