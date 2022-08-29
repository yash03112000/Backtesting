from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from User import *
from Indicators import Indicators as ind
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
        self.entryConditions = v2
        self.exitConditions = v3
        self.status = "BUY"
    
    def execute(self):
        now = dt.datetime.now()
        start = now - dt.timedelta(days = self.days)
        stock = self.instrument
        stock = stock + '.NS'
        self.df = pdr.get_data_yahoo(stock, start, now,interval=self.timeframe)
        print(self.df)
        self.time = []
        dateTime = self.df.index.tolist()
        for i in dateTime:
            timetemp =  i.strftime("%H:%M")
            self.time.append(timetemp)    
        self.user = User()
        fig = plt.figure()
        self.ax1 = fig.add_subplot(1,1,1)
        ani = animation.FuncAnimation(fig, self.animate, interval=0)
        plt.show()

    def animate(self,i):
        i+=1
        size = len(self.df['Close'])
        if(i<=size-1):
            self.xar = self.time[0:i+1]
            self.yar = self.df[0:i+1]
        elif(i==size):
            # self.user.exitProcedure(self.close[-1],self.time[i])
            pass
        
        if(i<=size-1):
            self.ax1.clear()
            self.ax1.plot(self.xar,self.yar['Close'])
            every_nth = 20
            for n, label in enumerate(self.ax1.xaxis.get_ticklabels()):
                if n % every_nth != 0:
                    label.set_visible(False)
            if(i>0):
                if(self.status=="BUY"):
                    if(self.evaluate(self.entryConditions)):
                        self.entryX.append(self.xar[-1])
                        self.entryY.append(self.yar['Close'][-1])
                        # user.shortSell(close[i],time[i])
                        print("BUY")
                        self.status = "SELL"
                        print(self.entryX)
                else:
                    if(self.evaluate(self.exitConditions)):                    
                        # user.buy(close[i],time[i])
                        self.exitX.append(self.xar[-1])
                        self.exitY.append(self.yar['Close'][-1])
                        print("SELL")
                        self.status = "BUY"
                        print(self.exitX)
                plt.scatter(self.exitX,self.exitY,color="red")
                plt.scatter(self.entryX,self.entryY,color="green")
                # # user.checkTargetAndStoploss(close[i],time[i])    

    def evaluate(self,conditions):
        result = []
        for i in conditions:
            operand1 = 0
            operand2 = i['value']
            operand = i['operand']
            operatorVar = i['operator']
            if(operand=='Close'):
                operand1 = self.yar['Close'][-1]
            elif(operand=='RSI'):
                operand1 = ind.RSIUtil(self.yar['Close'])
            elif(operand=='ADX'):
                operand1 = ind.ADXUtil(self.yar['High'],self.yar['Low'],self.yar['Close'])
            if(str(operand1)=='nan'):
                result.append(False)
                continue
            # print(operand1)
            result.append(self.evalOperator(operand1,operand2,operatorVar))
        # print(result)
        count  = 0
        for i in result:
            if(i==False):
                count+=1
        # print(count)
        if(len(result)>0 and count==0):
            return True
        else:
            return False
    
    @staticmethod
    def evalOperator(operand1,operand2,operator):
        if(operator=='<'):
            if(operand1<operand2):
                return True
            else:
                return False
        elif(operator=='<='):
            if(operand1<=operand2):
                return True
            else:
                return False
        elif(operator=='>'):
            if(operand1>operand2):
                return True
            else:
                return False
        elif(operator=='>='):
            if(operand1>=operand2):
                return True
            else:
                return False
        elif(operator=='=='):
            if(operand1==operand2):
                return True
            else:
                return False
                



