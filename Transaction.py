
class Transaction:
    enterPrice = 0
    volume = 0
    totalAmount = 0
    type = ""
    target = 0
    stoploss = 0
    targetP = 0.75
    stoplossP = 1
    enterTime = ""

    def __init__(self,enterPrice,volume,type,time):
        self.enterPrice = enterPrice
        self.volume = volume
        self.type = type
        self.enterTime = time
        self.totalAmount = enterPrice*volume
        if(type=="BUY"):
            self.target = enterPrice + (self.targetP*enterPrice)/100
            self.stoploss = enterPrice - (self.stoplossP*enterPrice)/100
        else:
            self.target = enterPrice - (self.targetP*enterPrice)/100
            self.stoploss = enterPrice + (self.stoplossP*enterPrice)/100