import datetime as dt
from turtle import color
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from scipy import signal as sc

from plot import *


yf.pdr_override() 
now = dt.datetime.now()
start = now - dt.timedelta(hours=40)
now = now - dt.timedelta(hours=20)


stock='OIL'
stock = stock + '.NS'



df = pdr.get_data_yahoo(stock, start, now,interval="1m")
close = df['Close']
time = []
dateTime = df.index.tolist()
for i in dateTime:
    timetemp =  i.strftime("%H:%M")
    time.append(timetemp)



plt.plot(time,close)
plt.scatter(maximaX,maximaY,color="green")
plt.scatter(minimaX,minimaY,color="red")
# plt.show()

plot(time,close,df)




