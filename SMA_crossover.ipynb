#dont forget to install the libaries!!!#

from bokeh.io import output_notebook
output_notebook()
import yfinance as yf
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ticker = input('Enter the ticker you want to test')
ticker_data = yf.Ticker(ticker)
price_data = ticker_data.history(interval='1h', period ='200d')
price_data = price_data.iloc[:-1] 

def Simple_Moving_Average(price, period):
    return pd.Series(price).rolling(period).mean()

class SMACrossOver(Strategy):
    interval_short_term = 50
    interval_long_term = 200
    
    def init(self):
        close = self.data.Close
        self.sma_short_term = self.I(Simple_Moving_Average, close, self.interval_short_term)
        self.sma_long_term = self.I(Simple_Moving_Average, close, self.interval_long_term)


    def next(self):
        price = self.data.Close[-1]

        if crossover(self.sma_short_term, self.sma_long_term,): #prosta srednia kroczaca z mniejszego przedzialu czasu przecina od dolu ta z dluzszego#
            self.buy()
        elif crossover(self.sma_long_term, self.sma_short_term,):#vice versa#
            if self.position:
                self.position.close()

backtest = Backtest(price_data, SMACrossOver, cash=10000, commission=0.002, exclusive_orders=True, finalize_trades = True) 
#Jeśli exclusive_orders = True, to nowa pozycja automatycznie zamyka poprzednia. Czyli maksymalnie mamy jeden trade naraz#
df = pd.DataFrame(backtest.run())
print(df)
backtest.plot
