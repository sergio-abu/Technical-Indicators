#### We will analize and explain all the technical indicators using the Alibaba Group Holding Ltd stock (BABA):

![BABA](STOCK.png)

1- [SMA (Simple Moving Average)](./SMA/)
###### SMA (Simple Moving Average) is a technical indicator that shows the average value of a security's price over a period of time. It's calculated by adding the closing price of a security for a number of time periods and then dividing this total by the number of time periods. It's used to identify trends, support and resistance levels.
![SMA](/SMA/SMA.png)


2- [EMA (Exponential Moving Average)](./EMA/)
###### EMA (Exponential Moving Average) is a technical indicator that shows the average value of a security's price over a period of time, but gives more weight to recent prices. It's calculated by applying a percentage weighting to the most recent price, where the weighting decreases exponentially with each previous period. EMA is used to identify trends, support and resistance levels in a similar way as SMA.
![EMA](/EMA/EMA.png)


3- [WMA (Weighted Moving Average)](./WMA/)
###### WMA (Weighted Moving Average) is a type of moving average that assigns different weights to the data points used to calculate the average. The most recent data points are given more weight, while older data points are given less weight.

###### For example, if a WMA has a period of 20, it would use the last 20 data points to calculate the average, but the most recent data point would have a higher weight than the oldest data point.

###### WMA is generally used to reduce the lag time in moving averages and make the average more responsive to recent price changes. It is particularly useful in identifying short-term trends and making more accurate predictions about future price movements.

###### WMA is similar to EMA (Exponential Moving Average) in that both assign more weight to recent data points, but the way the weight is assigned is different. EMA uses an exponential decay factor to assign weight to data points, while WMA assigns weights based on a linear weighting scheme.
![WMA](/WMA/WMA.png)


4- [VWAP (Volume Weighted Average Price)](./VWAP/)
###### VWAP (Volume Weighted Average Price) is a technical indicator that calculates the average price of a security based on the volume traded. It is calculated by summing the product of the price and volume for each trade, and then dividing that by the total volume traded.

###### VWAP is often used by traders as a benchmark for intraday trading, as it accounts for both price and volume. It can help traders identify trends and make more informed trading decisions by providing a clear picture of the stock's historical trading activity.

###### VWAP can be used on different timeframes such as intraday, daily, weekly or monthly, and can be used for different types of assets such as stocks, futures, options, etc.

###### One of the main differences between VWAP and other moving averages like SMA, EMA, and WMA is that the latter ones are based solely on price, whereas VWAP takes into account both price and volume.

###### VWAP is commonly used in algorithmic trading strategies and by portfolio managers as a benchmark to evaluate the performance of their trades. It can also be used to identify buying and selling pressure in the market, by comparing the current price to the VWAP.
![VWAP](/VWAP/VWAP.png)


5- [MACD (Volume Weighted Average Price)](./MACD/)
###### MACD (Moving Average Convergence Divergence) is a technical indicator that is used to identify changes in the momentum and trend of a security. It is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA. The resulting difference is then plotted on a graph as a histogram, with a signal line that is a 9-period EMA of the histogram.
###### The MACD is typically shown on a separate graph below the main price chart, with the histogram representing the difference between the two moving averages, and the signal line is used as a trigger for buy and sell signals. When the MACD line crosses above the signal line, it is considered a bullish signal and indicates that the security may be about to rise in value. Conversely, when the MACD line crosses below the signal line, it is considered a bearish signal and indicates that the security may be about to fall in value.
![MACD](/MACD/MACD.png)


6- [Stoch (Stochastic Oscillator)](./STOCH/)
###### The Stochastic Oscillator (Stoch) is a momentum indicator that compares the closing price of a security to its price range over a given period of time. It is typically shown as two lines on a separate graph below the main price chart, with one line called the %K and the other called the %D.
###### The %K line is the current stochastic value, and it is calculated by comparing the closing price of a security to its price range over a certain number of periods. The %D line is a moving average of the %K line and is used as a signal line to generate buy and sell signals.
###### When the %K line crosses above the %D line, it is considered a bullish signal, indicating that the security may be about to rise in value. Conversely, when the %K line crosses below the %D line, it is considered a bearish signal, indicating that the security may be about to fall in value.
###### Stochastic oscillator is a momentum indicator that helps to identify overbought and oversold conditions in the market. An overbought condition is indicated when the %K line is above 80, and an oversold condition is indicated when the %K line is below 20.
![STOCH](/STOCH/STOCH.png)


7- [RSI (Relative Strength Index)](./RSI/)
###### The Relative Strength Index (RSI) is a momentum indicator that compares the magnitude of recent gains to recent losses in order to determine overbought and oversold conditions of an asset. It is typically used to identify short-term price trends and to generate buy and sell signals.
###### The RSI is calculated using a formula that compares the average gains and losses of an asset over a given period of time. The RSI ranges from 0 to 100, with values above 70 indicating that an asset is overbought and values below 30 indicating that an asset is oversold.
###### When the RSI is above 70, it suggests that the asset is becoming overbought and that the price may be due for a correction. Conversely, when the RSI is below 30, it suggests that the asset is becoming oversold and that the price may be due for a rebound.
![RSI](/RSI/RSI.png)

