import datetime as dt
import pandas as pd
import StrategyWindows.Window1 as strategyw1
import StrategyWindows.Window2 as strategyw2
import StrategyWindows.Window3 as strategyw3
import ScreenerWindows.Window1 as screenerw1
import ScreenerWindows.Window2 as screenerw2
import SarimaWindows.Window1 as sarimaw1
import LandingWindow as landingw
from Strategy import *
from Screener import *
from Sarima import *

yf.pdr_override() 

main_window = landingw.Window1()
main_window.execute()
key = main_window.getValues()
print(key)


if(key=="Screener"):
    w1 = screenerw1.Window1()
    w1.execute()
    w2 = strategyw2.Window2()
    w2.execute()
    values1 = w1.getValues()
    values2 = w2.getValues()
    screener = Screener(values1,values2)
    screener.execute()
elif(key=="Strategy"):
    w1 = strategyw1.Window1()
    w1.execute()
    w2 = strategyw2.Window2()
    w2.execute()
    w3 = strategyw3.Window3()
    w3.execute()
    values1 = w1.getValues()
    values2 = w2.getValues()
    values3 = w3.getValues()
    strategy = Strategy(values1,values2,values3)
    strategy.execute()
else:
    w1 = sarimaw1.Window1()
    w1.execute()
    values = w1.getValues()
    print(values)
    sarima = Sarima(values)
    sarima.execute()











