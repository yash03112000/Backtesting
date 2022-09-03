
# Equity Screening, Backtesting and Forecasting Platform

A python platform, where user can use several technichal indices 
to provide entry and exit conditions to screen stocks, design strategies, backtest them
and forecast future prices of stock.


## Features
- Use Technichal Indices like **Supertrend, RSI, ADX**
- Several Charts like **OHLC, Heikin Ashi**
- Select between multiple timeframes
- Work with hundreds of NSE listed stocks
Screener
- Choose among several popular indices lists like NIFTY50, NIFTYBANK etc
- Provide Entry Conditions using our condition engine
- The application will return all the equites satisfying the entry conditions
Strategy
- Design your trading strategies and back test them over the user specified period
- Get visualisation of all entry and exit positions through an animated plot
- Go **Long or Short** on the basis of your requirements
- Both **CNC**(Long term) and **MIS**(Intraday Trading) products are supported
Forecasting
- Use **SARIMA** model to forecast future prices of the stock
- The model will go though prices trends of previous 2 years and analyse them to predict future prices
**Some Geeky Stuff**
- Incorporated **Augmented dickey fuller test** to determine whether the data is staionary
- Using **Akaike Information Criterion** to optimise model parameters on the basis of lowest aic score


## Installation

Install Following Python Libraries

```bash
pandas
numpy
matplotlib
mplfinance
TA-Lib
tkinter
statsmodel
datetime
pmdarima
yfinance
```

Clone the repository and run following command
```bash
python3 main.py
```
## Disclaimer
- This is a Minimum viable product and user can interact many bugs
- Proper error logging is still to be implemented
- User can play with provided spreadsheets to add more stocks and list
- This application uses both tkinter GUI, result sheets and terminal prompt to provide update



## 🚀 About Me
I'm final year undergraduate at IIT Kanpur. I got inspired to build this platform while
using several applications like Zerodha's [Streak](https://www.streak.tech) and [Tradetron](https://tradetron.tech/).

I like solving problems faced in my daily life through my coding skills. Whether its 
- [Minlinks](https://github.com/yash03112000/minlink) - A platform to save and share links in today's world
- [Mafia](https://github.com/yash03112000/mafia) - A online version of popular game to play with friends when we can't play in person due to pandemic

I prefer framing the problem and start working to solve them
Vist my [IITK](https://home.iitk.ac.in/~yashag/) homepage to know more about my work

Feel free to contact me at yashag@iitk.ac.in to discuss more about my and your interest, especially about this platform.

Kindly do suggest me some cool name for this application