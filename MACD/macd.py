#%%
from openbb_terminal.sdk import openbb
import pandas as pd


STOCK = openbb.stocks.load('BABA')

VWAP = openbb.ta.macd(pd.Series(STOCK['Close']))
VWAP.plot()
# %%
