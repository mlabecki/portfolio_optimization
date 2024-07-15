import pandas as pd
import yfinance as yf
import requests
import json
import os
from convert_date import *

s = requests.Session()

max_tickers = 30

# user-agent from https://useragentstring.com/
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
res = s.get("https://api.nasdaq.com/api/quote/list-type/nasdaq100", headers=headers)

main_data = res.json()['data']['data']['rows']

if res.status_code == 200:

    main_data = res.json()['data']['data']['rows']
    df_index = range(len(main_data))
    df_final_index  = range(max_tickers)
    
    df_market_cap = pd.DataFrame(columns=['Symbol', 'Market Cap'], index=df_index)
    df_final = pd.DataFrame(columns=['Symbol', 'Company Name', 'Market Cap'], index=df_final_index)

    for i in df_index:
    
        md = main_data[i]
        df_market_cap.loc[i, 'Symbol'] = md['symbol']
        df_market_cap.loc[i, 'Market Cap'] = md['marketCap'].replace(',', '')
    
    df_market_cap['Market Cap'] = df_market_cap['Market Cap'].astype('Int64')
    df_market_cap = df_market_cap.sort_values(by='Market Cap', ascending=False)
    df_market_cap = df_market_cap.reset_index(drop=True)
    df_market_cap = df_market_cap[: max_tickers]

    df_final['Symbol'] = df_market_cap['Symbol']
    df_final['Market Cap'] = df_market_cap['Market Cap']

    for i in df_final_index:

        ticker = df_final.loc[i, 'Symbol']
        short_name = yf.Ticker(ticker).info['shortName']
        long_name = yf.Ticker(ticker).info['longName']
        company_name = short_name if len(short_name) <= len(long_name) else long_name
        df_final.loc[i, 'Company Name'] = company_name
        
    print(df_final)
