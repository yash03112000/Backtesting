from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
import numpy as np
from tqdm import tqdm_notebook
import pandas as pd
from itertools import product
import pmdarima as pm
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset


class Sarima:
    def __init__(self,values):
        self.instrument = values
    def execute(self):
        now = dt.datetime.now()
        start = now - dt.timedelta(days = 2*365)
        stock = self.instrument
        stock = stock + '.NS'
        print(stock)
        try:
            self.df = pdr.get_data_yahoo(stock, start, now,interval='1d')
        except Exception:
            print("Please enter a valid NSE stock acronym")
            exit()
        close = self.df['Close']
        # print(self.df)
        model = pm.auto_arima(close, d = 1, start_p = 0, start_q = 0, max_p = 2, max_q = 2, start_P = 0, start_Q = 0, max_P = 2, max_Q = 2,
         D = 1, seasonal = True, m = 4, stepwise = True, trace = False, suppress_warnings = True)
        print(model.summary())
        best_model = SARIMAX(close, order=model.order, seasonal_order=model.seasonal_order).fit(dis=-1)
        fit = best_model.fittedvalues
        fit[:5] = np.NaN
        pred_date2=[close.index[-1]+ DateOffset(days = x)for x in range(0,61)]
        pred_date=pd.DataFrame(index=pred_date2[1:])
        start = close.shape[0]
        close = pd.concat([close,pred_date])
        print(close)
        end = close.shape[0]
        print(end-start)
        forecast = best_model.predict(start=start, end=end)
        forecast.index = pred_date2
        forecast = fit.append(forecast)
        print(forecast)
        plt.plot(close, label='actual')
        plt.plot(forecast, color='r', label='model')
        plt.legend()
        plt.show()


