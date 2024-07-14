import yfinance as yf
import pandas as pd
import numpy as np
from mapping_tickers import *
from datetime import datetime, timedelta
import os
import scipy.optimize


# In VS Code must save the workspace before a custom module can be properly imported

# tickers = ['SPY', 'BND', 'GLD', 'QQQ', 'VTI']
# tickers = ['^SPX', '^GSPC', '^GSPTSE', '^DJI', ' ^NDX', '^IXIC', '^MOVE']
# ^SPX is essentially the same as ^GSPC (S&P 500) - same numbers
# ^GSPTSE is S&P/TSX Composite index
# ^IXIC is NASDAQ Composite (> 2500 stocks), ^NDX is NASDAQ-100 Index (100 stocks)
# ^DJI is Dow Jones Industrial Average. You cannot invest in ^DJI itself, 
# but you can invest in DJIA, which is an ETF holding DJIA stocks
# and selling call options on the underlying (covered call strategy).
# QQQ is Invesco QQQ Trust, an ETF investing in NASDAQ-100 Index.

df_djia = pd.DataFrame()

djia_tickers = list(djia_components.keys())

for t in djia_tickers:
    data = yf.download(t)
    df_djia[t] = data['Adj Close']
    df_djia_nonan = df_djia.dropna()


if __name__ == '__main__':
    print(df_djia_nonan)
