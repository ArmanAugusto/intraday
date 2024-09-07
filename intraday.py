import pandas as pd
import sqlite3
import requests

def fetch_intraday_data(ticker, interval='1min'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}={api}&outputsize=full'
    response = requests.get(url)
    data = response.json()
    
    time_series = data.get(f'Time Series ({interval})', {})
    if not time_series:
        print(f'No data returned for {ticker}')
        return None
    
    df = pd.DataFrame(time_series).T
    df.index.name = 'timestamp'
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.sort_index()
    df.reset_index(inplace=True)
    df['ticker'] = ticker

    return df
