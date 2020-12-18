from db import CreateRecord
from marketstack import EndOfDayAPI


if __name__=="__main__":
    ticker_list = ['AAPL', 'C', 'UAL', 'MMM']

    for ticker in ticker_list:
        eod_data = EndOfDayAPI().get(ticker)
        CreateRecord().stock_eod_price(
            stock_ticker=eod_data['symbol'],
            eod_date=eod_data['date'],
            open_price=eod_data['open'],
            eod_price=eod_data['close']
        )
