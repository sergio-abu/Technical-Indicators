#%%
from openbb_terminal.sdk import openbb
import pandas as pd


STOCK = openbb.stocks.load('BABA')

# close series, default period = 50, default offset = 0
EMA = openbb.ta.ema(pd.Series(STOCK['Close']))


STOCK.plot(y='Close')
EMA.plot()
# %%
