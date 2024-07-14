import yfinance as yf
import pandas as pd

symbol = 'AAPL'
stock = pd.DataFrame(yf.download(symbol)['Adj Close'])
stock = stock.reset_index()

tk = yf.Ticker(symbol)
tk_expirations = list(tk.options)
tk_calls = tk.option_chain().calls
tk_puts = tk.option_chain().puts
tk_underlying = tk.option_chain().underlying
tk_underlying_price = tk_underlying['regularMarketPrice']

price_strike_spread = 10
df_tk_calls = pd.DataFrame()
df_tk_puts = pd.DataFrame()

for exp in tk_expirations:

    df_c = pd.DataFrame(tk.option_chain(exp).calls)
    df_c = df_c.reset_index(drop=True)
    cond_c1 = df_c['strike'] - tk_underlying_price <= price_strike_spread
    cond_c2 = df_c['strike'] - tk_underlying_price >= -price_strike_spread
    df_c = df_c[cond_c1 & cond_c2]
    df_tk_calls = pd.concat([df_tk_calls, df_c])

    df_p = pd.DataFrame(tk.option_chain(exp).puts)
    df_p = df_p.reset_index(drop=True)
    cond_p1 = df_p['strike'] - tk_underlying_price <= price_strike_spread
    cond_p2 = df_p['strike'] - tk_underlying_price >= -price_strike_spread
    df_p = df_p[cond_p1 & cond_p2]
    df_tk_puts = pd.concat([df_tk_puts, df_p])

df_tk_calls = df_tk_calls.reset_index(drop=True)
df_tk_puts = df_tk_puts.reset_index(drop=True)

print(df_tk_calls)
print(df_tk_puts)
    

