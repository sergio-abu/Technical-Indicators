#%%
from openbb_terminal.sdk import openbb
import pandas as pd


STOCK = openbb.stocks.load('BABA')

VWAP = openbb.ta.stoch(STOCK)
VWAP.plot()
# %%
