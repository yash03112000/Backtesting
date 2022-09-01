import talib as ta
import pandas as pd
import numpy as np

class Indicators:
    @staticmethod
    def RSIUtil(close):
        return ta.RSI(close,timeperiod=14)[-1]
    @staticmethod
    def ADXUtil(high,low,close):
        return ta.ADX(high,low,close,timeperiod=14)[-1]
    @staticmethod
    def Supertrend(df):
        
        high = df['High']
        low = df['Low']
        close = df['Close']
        atr_period = 10
        multiplier = 3
        
        price_diffs = [high - low, 
                    high - close.shift(), 
                    close.shift() - low]
        true_range = pd.concat(price_diffs, axis=1)
        true_range = true_range.abs().max(axis=1)
        atr = true_range.ewm(alpha=1/atr_period,min_periods=atr_period).mean() 
        
        hl2 = (high + low) / 2
        final_upperband = hl2 + (multiplier * atr)
        final_lowerband = hl2 - (multiplier * atr)
        
        supertrend = [True] * len(df)
        
        for i in range(1, len(df.index)):
            curr, prev = i, i-1
            
            if close[curr] > final_upperband[prev]:
                supertrend[curr] = True
            elif close[curr] < final_lowerband[prev]:
                supertrend[curr] = False
            else:
                supertrend[curr] = supertrend[prev]
                
                if supertrend[curr] == True and final_lowerband[curr] < final_lowerband[prev]:
                    final_lowerband[curr] = final_lowerband[prev]
                if supertrend[curr] == False and final_upperband[curr] > final_upperband[prev]:
                    final_upperband[curr] = final_upperband[prev]

            if supertrend[curr] == True:
                final_upperband[curr] = np.nan
            else:
                final_lowerband[curr] = np.nan
        
        return pd.DataFrame({
            'Supertrend': supertrend,
            'Final Lowerband': final_lowerband,
            'Final Upperband': final_upperband
        }, index=df.index)    


