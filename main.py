import datetime as dt
import pandas as pd
from Window1 import Window1
from Window1 import *
from Window2 import *
from Window3 import *
from Strategy import *


yf.pdr_override() 

w1 = Window1()
w1.execute()
w2 = Window2()
w2.execute()
w3 = Window3()
w3.execute()
values1 = w1.getValues()
values2 = w2.getValues()
values3 = w3.getValues()

strategy = Strategy(values1,values2,values3)
strategy.execute()












# Sell/Buy when other peak appears without waiting for stoploss