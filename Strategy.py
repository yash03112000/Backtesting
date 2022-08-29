from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from User import *
from Indicators import Indicators as ind
class Strategy:
    def __init__(self,v1,v2,v3):
        self.name = v1[0]
        self.chart = v1[1]
        self.days = v1[2]
        self.instrument = v1[3]
        self.timeframe = v1[4]
        self.entryConditions = v2
        self.exitConditions = v3
        self.status = "BUY"
    
    def execute(self):
        now = dt.datetime.now()
        start = now - dt.timedelta(days = self.days)
        stock = self.instrument
        stock = stock + '.NS'
        df = pdr.get_data_yahoo(stock, start, now,interval=self.timeframe)
        print(df)
        self.close = []
        self.time = []
        self.close = df['Close']
        dateTime = df.index.tolist()
        for i in dateTime:
            timetemp =  i.strftime("%H:%M")
            self.time.append(timetemp)    
        self.user = User()
        fig = plt.figure()
        fig = plt.figure()
        self.ax1 = fig.add_subplot(1,1,1)
        ani = animation.FuncAnimation(fig, self.animate, interval=0)
        plt.show()

    def animate(self,i):
        i+=1
        size = len(self.close)
        if(i<=size-1):
            self.xar = self.time[0:i+1]
            self.yar = self.close[0:i+1]
        elif(i==size):
            self.user.exitProcedure(self.close[-1],self.time[i])
        
        if(i<=size-1):
            self.ax1.clear()
            self.ax1.plot(self.xar,self.yar)
            every_nth = 20
            for n, label in enumerate(self.ax1.xaxis.get_ticklabels()):
                if n % every_nth != 0:
                    label.set_visible(False)
            if(i>0):
                if(self.status=="BUY"):
                    self.evaluate(self.entryConditions)
                else:
                    self.evaluate(self.exitConditions)
                entryY = []
                entryX = []
                exitY = []
                exitX = []

                # for ind in indices[0]:
                #     entryY.append(self.close[ind])
                #     entryX.append(self.time[ind])

                # for ind in indices[1]:
                #     exitY.append(self.close[ind])
                #     exitX.append(time[ind])
                # plt.scatter(minimaX,minimaY,color="red")
                # plt.scatter(maximaX,maximaY,color="green")
                # # user.checkTargetAndStoploss(close[i],time[i])
                # if(indices[2]=="MAXIMA"):
                #     user.shortSell(close[i],time[i])
                # elif(indices[2]=="MINIMA"):
                #     user.buy(close[i],time[i])
    
    def evaluate(self,conditions):
        result = []
        for i in conditions:
            operand1 = 0
            operand2 = i['value']
            operand = i['operand']
            if(operand=='Close'):
                operand1 = self.yar[-1]
            elif(operand=='RSI'):
                ind.RSIUtil(self.yar)



