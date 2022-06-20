import datetime as dt
from turtle import color
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from scipy import signal as sc

from plot import *


yf.pdr_override() 
now = dt.datetime.now()
start = now - dt.timedelta(hours=69)
now = now - dt.timedelta(hours=44)


stock='OIL'
stock = stock + '.NS'



df = pdr.get_data_yahoo(stock, start, now,interval="1m")
time = []




# plt.plot(time,close)

# plt.show()

plot(df)




# Sell/Buy when other peak appears without waiting for stoploss