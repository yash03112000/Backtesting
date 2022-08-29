import talib as ta
class Indicators:
    @staticmethod
    def RSIUtil(close):
        return ta.RSI(close,timeperiod=14)
    @staticmethod
    def ADXUtil(close):


