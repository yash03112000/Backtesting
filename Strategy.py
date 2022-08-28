from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
import pandas as pd


# now = dt.datetime.now()
# start = now - dt.timedelta(hours=93)
# now = now - dt.timedelta(hours=68)


# stock='OIL'
# stock = stock + '.NS'



df = pdr.get_data_yahoo(stock, start, now,interval="1m")
class Strategy:
    def __init__(self,v1,v2,v3):
        pass

