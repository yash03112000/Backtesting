import math
import pandas as pd

from Transaction import Transaction
class User:

    balance = 2000

    activeTransactions = []
    transactions = pd.DataFrame({'Type':[],'EnterTime':[],'EnterPrice':[],'ExitPrice':[],'ExitTime':[],'Volume':[],'P/L':[]})

    def buy(self,price,time):
        totalCapacity = math.floor(self.balance/price)
        volume = totalCapacity
        if(volume>0):
            self.balance -= price*volume
            transaction = Transaction(price,volume,"BUY",time)
            self.activeTransactions.append(transaction)
    def shortSell(self,price,time):
        totalCapacity = math.floor(self.balance/price)
        volume = totalCapacity
        if(volume>0):
            self.balance -= price*volume
            transaction = Transaction(price,volume,"SELL",time)
            self.activeTransactions.append(transaction)
    def checkTargetAndStoploss(self,price,time):
        for i in self.activeTransactions:
            if i.type == "BUY":
                if(price > i.target or price < i.stoploss):
                    self.exitStock(price,i,time)
            if i.type == "SELL":
                if(price < i.target or price > i.stoploss):
                    self.exitStock(price,i,time)

    def exitProcedure(self,price,time):
        for i in self.activeTransactions:
            self.exitStock(price,i,time)
        self.transactions.to_excel("result.xlsx")
        net = 0
        for i in self.transactions['P/L']:
            net+=i
        self.balance+=net
        print("Final Balance:", self.balance)
        # exit()
    def exitStock(self,price,transaction,time):
        self.balance += transaction.totalAmount
        self.activeTransactions.remove(transaction)
        pl = transaction.volume*(price-transaction.enterPrice)
        if transaction.type == "SELL":
            pl = -pl 
        df = pd.DataFrame({'Type':[transaction.type],'EnterTime':[transaction.enterTime],'EnterPrice':[transaction.enterPrice],'ExitPrice':[price],'ExitTime':[time],'Volume':[transaction.volume],'P/L':[pl]})
        self.transactions = pd.concat([self.transactions,df])
