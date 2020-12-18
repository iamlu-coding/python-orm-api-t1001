from peewee import *
import config


database = PostgresqlDatabase(
    database=config.DATABASES['NAME'],
    user=config.DATABASES['USER'],
    password=config.DATABASES['PASSWORD'],
    host=config.DATABASES['HOST'],
    port=config.DATABASES['PORT']
    )

class BaseModel(Model):
    class Meta:
        database = database

class StockEODPrice(BaseModel):
    id = AutoField()
    stock_ticker = CharField(max_length=6)
    eod_date = DateTimeField()
    open_price = DecimalField(max_digits=14, decimal_places=7)
    eod_price = DecimalField(max_digits=14, decimal_places=7)
    created_date = DateTimeField(constraints=[SQL("Default now()")], null=False)

    class Meta:
        table_name = 'stock_eod_price'