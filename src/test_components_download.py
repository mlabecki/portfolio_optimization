import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from convert_date import *

s = requests.Session()

# s.headers.update({
#    "Accept-Language": "en-US,en;q=0.9", 
#    "Accept-Encoding": "gzip, deflate, br",
#    "User-Agent": "Java-http-client/"
# })
# r = s.get("https://www.nasdaq.com/market-activity/quotes/nasdaq-ndx-index")
# soup = BeautifulSoup(r.content, "html.parser")
# res = json.loads([x for x in soup.find("script", {"type": "application/json"})][0])

# headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

headers = {'user-agent': 'Chrome/126.0.6478.127'}
res = s.get("https://api.nasdaq.com/api/quote/list-type/nasdaq100", headers=headers)
print(res.headers)
main_data = res.json()['data']['data']['rows']

df_data = pd.DataFrame(columns=['Symbol', 'Company Name', 'Market Cap'])
for i in range(len(main_data)):
    md = main_data[i]
    print(md['symbol'], md['companyName'], md['marketCap'])