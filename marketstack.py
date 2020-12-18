import requests
from config import MS_ACCESS_KEY

class EndOfDayAPI:
    def get(self, stock_ticker):

        params = {
            'access_key': MS_ACCESS_KEY
        }
        url = 'http://api.marketstack.com/v1/tickers/{0}/eod/latest'.format(stock_ticker)
        results = requests.get(url, params=params)

        return results.json()

class RealTimeAPI:
    def get(self):
        pass