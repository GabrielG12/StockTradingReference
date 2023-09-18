import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries


#TODO: DATA PREPARATION

def get_stock(stock_name: str, api_key: str, range_type: str, range_: int):
    ts = TimeSeries(key=api_key, output_format="pandas")

    if range_type == 'daily':
        try:
            df, meta_data = ts.get_daily(symbol=stock_name, outputsize="full")
            df = df["4. close"][0:range_ + 1]
            df = df[::-1]
        except Exception as e:
            print(f"An error occurred: {e}")

    return df
