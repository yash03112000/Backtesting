from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from Orderbook import *
from Utils.ConditionChecker import ConditionChecker as cnd
from Utils.HeikinAshi import HeikinAshi as ha

class Strategy:

    entryY = []
    entryX = []
    exitY = []
    exitX = []
    def __init__(self,v1,v2,v3):
        self.name = v1[0]
        self.chart = v1[1]
        self.days = v1[2]
        self.instrument = v1[3]
        self.timeframe = v1[4]
        self.volume = v1[5]
        self.tradetype = v1[6]
        self.product = v1[7]
        self.entryConditions = v2
        self.exitConditions = v3
        self.status = "ENTRY"
    
    def execute(self):
        now = dt.datetime.now()
        start = now - dt.timedelta(days = self.days)
        stock = self.instrument
        stock = stock + '.NS'
        self.df = pdr.get_data_yahoo(stock, start, now,interval=self.timeframe)
        if(self.chart=="Heikin-Ashi"):
            self.df = ha.convert(self.df)
        self.time = []
        # print(self.df)
        self.dateTime = self.df.index.tolist()
        for i in self.dateTime:
            timetemp =  i.strftime("%H:%M")
            self.time.append(timetemp)
        fig = plt.figure()
        self.ax1 = fig.add_subplot(1,1,1)
        self.ax1.plot(self.dateTime,self.df['Close'])
        ani = animation.FuncAnimation(fig, self.animate, interval=0)
        self.orderbook = Orderbook(self.volume,self.tradetype)        
        plt.show()

    def animate(self,i):
        size = len(self.df['Close'])
        if(i<size-1):
            self.xar = self.dateTime[0:i+1]
            self.yar = self.df[0:i+1]
            if(self.product=="MIS"):
                time1 = int(self.time[i].split(':')[0])
                time1 += (int(self.time[i].split(':')[1]))/100
                time2 = int(self.time[i+1].split(':')[0])
                time2 += (int(self.time[i+1].split(':')[1]))/100
                if(time1 > 15.15):
                    return
                if(time2==9.15 or time2>15.15):
                    self.orderbook.intradayExit(self.df['Close'][-1],self.xar[-1])
                    self.status = "ENTRY"
                    return
        elif(i==size):
            self.orderbook.exitProcedure(self.df['Close'][-1],self.dateTime[-1])
            self.status = "ENTRY"
        if(i<size-1):
            self.ax1.clear()
            self.ax1.plot(self.xar,self.yar['Close'])
            every_nth = 20
            for n, label in enumerate(self.ax1.xaxis.get_ticklabels()):
                if n % every_nth != 0:
                    label.set_visible(False)
            if(self.status=="ENTRY"):
                if(cnd.evaluate(self.yar,self.entryConditions)):
                    self.entryX.append(self.xar[-1])
                    self.entryY.append(self.yar['Close'][-1])
                    self.orderbook.entry(self.yar['Close'][-1],self.xar[-1])
                    print("BUY")
                    self.status = "EXIT"
                    # print(self.entryX)
                    self.orderbook.entry(self.entryY[-1],self.entryX[-1])
            else:
                if(cnd.evaluate(self.yar,self.exitConditions)):                    
                    self.exitX.append(self.xar[-1])
                    self.exitY.append(self.yar['Close'][-1])
                    print("SELL")
                    self.status = "ENTRY"
                    # print(self.exitX)
                    self.orderbook.exit(self.yar['Close'][-1],self.xar[-1])
            plt.scatter(self.exitX,self.exitY,color="red")
            plt.scatter(self.entryX,self.entryY,color="green")

                



