import talib as ta
class Indicators:
    @staticmethod
    def RSIUtil(close):
        return ta.RSI(close,timeperiod=14)[-1]
    @staticmethod
    def ADXUtil(high,low,close):
        return ta.ADX(high,low,close,timeperiod=14)[-1]


