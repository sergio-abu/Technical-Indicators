#%%
from openbb_terminal.sdk import openbb
import pandas as pd


STOCK = openbb.stocks.load('BABA')

# close series, default period = 50, default offset = 0
SMA = openbb.ta.sma(pd.Series(STOCK['Close']))


STOCK.plot(y='Close')
SMA.plot()
# %%
