from models import StockEODPrice

class CreateRecord:
    def stock_eod_price(self, **kwargs):
        StockEODPrice.create(
            stock_ticker=kwargs['stock_ticker'],
            eod_date=kwargs['eod_date'],
            open_price=kwargs['open_price'],
            eod_price=kwargs['eod_price']
        )

class UpdateRecord:
    def stock_eod_price(self):
        pass

class DeleteRecord:
    def stock_eod_price(self):
        pass

class ReadRecord:
    def stock_eod_price(self):
        pass