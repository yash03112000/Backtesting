from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from Orderbook import *
from Utils.ConditionChecker import ConditionChecker as cnd


class Screener:

    screenedStocks = pd.DataFrame({'Stocks':[]})
    
    def __init__(self,v1,v2):
        self.name = v1[0]
        self.chart = v1[1]
        self.timeframe = v1[2]
        self.index = v1[3]
        self.entryConditions = v2
    
    def execute(self):
        now = dt.datetime.now()
        start = now - dt.timedelta(days = 7)
        filePath=r"./Spreadsheats/stocksList.xlsx"
        stocklist = pd.read_excel(filePath)[self.index]
        stocklist = [i for i in stocklist if str(i)!='nan']
        for i in stocklist:
            try:
                print(i)
                stock = i + '.NS'
                self.df = pdr.get_data_yahoo(stock, start, now,interval=self.timeframe)
                if(cnd.evaluate(self.df,self.entryConditions)):
                    df = pd.DataFrame({'Stocks':[stock]})
                    filePath = r"./Spreadsheats/result.xlsx"
                    self.screenedStocks = pd.concat([self.screenedStocks,df])
            except Exception:
                print("No Data found for "+ i)
        self.screenedStocks.to_excel(filePath)
        print(self.screenedStocks)

