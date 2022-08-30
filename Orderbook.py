import math
import pandas as pd

from Transaction import Transaction

class Orderbook:

    netPL = 0
    transactions = pd.DataFrame({'Type':[],'EnterTime':[],'EnterPrice':[],'ExitPrice':[],'ExitTime':[],'Volume':[],'P/L':[],'Net P/L':[]})
    activeTransactions = None
    def __init__(self,volume,tradetype):
        self.volume = volume
        self.tradetype = tradetype
    
    def entry(self,price,time):
        transaction = Transaction(price,time)
        self.activeTransactions = transaction
        print(self.activeTransactions.enterPrice)
        print(self.activeTransactions.enterTime)


    def exitProcedure(self,price,time):
        if(self.activeTransactions!=None):
            self.exit(price,time)
            self.activeTransactions = None
        print("Final P/L:", self.netPL)

    def intradayExit(self,price,time):
        if(self.activeTransactions!=None):
            self.exit(price,time)
            self.activeTransactions = None

    

    def exit(self,price,time):
        transaction = self.activeTransactions
        self.activeTransactions = None
        pl = self.volume*(price-transaction.enterPrice)
        if self.tradetype == "Short":
            pl = -pl
        self.netPL+=pl 
        df = pd.DataFrame({'Type':[self.tradetype],'EnterTime':[transaction.enterTime],'EnterPrice':[transaction.enterPrice],'ExitPrice':[price],'ExitTime':[time],'Volume':[self.volume],'P/L':[pl],'Net P/L':[self.netPL]})
        self.transactions = pd.concat([self.transactions,df])
        print(self.transactions)
        filePath = r"./Spreadsheats/result.xlsx"
        # self.transactions.to_excel(filePath)

