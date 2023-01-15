#%%
from openbb_terminal.sdk import openbb
import pandas as pd


STOCK = openbb.stocks.load('BABA')
print(STOCK)
RSI = openbb.ta.rsi(pd.Series(STOCK['Close']))
RSI.plot()

# %%
