from typing import Union
from fastapi import FastAPI,status,Response
from src.currency_lister import CurrencyList
from src.currency_converter import CurrencyConverter
from src.time_series_currency import TimeSeries

DESCRIPTION = """
This is a simple open source application that allows you to fetch currency conversion data.
You can just provide two currencies and get the conversion as output.
For suggestions and contributions, please visit [github.com/sagnik-sudo/Quick-Curr-Exchange](https://github.com/sagnik-sudo/Quick-Curr-Exchange/issues)
If you like my work, please star it on [github.com/sagnik-sudo/Quick-Curr-Exchange](https://github.com/sagnik-sudo/Quick-Curr-Exchange)
"""

app = FastAPI(
    title="Quick Curr Exchange",
    description=DESCRIPTION,
    version="Beta",
    docs_url="/",
    redoc_url="/currencies/redoc",
    contact={
        "name": "Developer - Sagnik Das",
        "email": "sagnikdas2305@gmail.com",
    },
)


@app.options("/supportedcurrencies",
             tags=["Currency Conversion"],
             name="Fetches list of supported Currencies")
async def get_currencies(response: Response):
    """
    Get the list of currencies supported by this application
    """
    try:
        currobj = CurrencyList()
        output = currobj.fetch()
        return output
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Could not fetch supported currencies"}

@app.post("/convert", tags=["Currency Conversion"],
          name="Convert a amount from local currency to another currency (Live or for a specific date)")
async def convert(from_currency_code, to_currency_code, amount,response: Response, date: Union[str, None] = None):
    """
    Convert a local currency amount to another currency amount >> Live or for a specific date
    Date Format is YYYY-MM-DD
    """
    try:
        from_currency_code = from_currency_code.upper()
        to_currency_code = to_currency_code.upper()
        currobj = CurrencyConverter()
        output = currobj.convert(
            from_currency_code, to_currency_code, amount, date)
        return output
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Wrong Input entered or invalid Currency"}


@app.post("/historicalrates", tags=["Currency Conversion"],
          name="Get conversions for a given currency on a particular date (back till 1999)")
async def historical_rates(from_currency_code,response: Response, date: Union[str, None] = None):
    """
    Get historical rates for a given currency (back till 1999)
    Date Format is YYYY-MM-DD
    """
    try:
        from_currency_code = from_currency_code.upper()
        currobj = CurrencyConverter()
        output = currobj.historical_rates(from_currency_code, date)
        return output
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Wrong Input entered or invalid Currency"}


@app.post("/timeseriesanalysis", tags=["Currency Conversion"],
          name="View time series analysis for a given pair of currencies and dates")
async def timeseriesanalysis(from_currency_code, to_currency_code, start_date, end_date,response: Response):
    """
    View time series analysis for a given pair of currencies and dates
    Date Format is YYYY-MM-DD
    Maximum Date Range is 1 year from start_date to end_date
    """
    try:
        from_currency_code = from_currency_code.upper()
        to_currency_code = to_currency_code.upper()
        currobj = TimeSeries(start_date, end_date,
                            from_currency_code, to_currency_code)
        output = currobj.fetch()
        return output
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Wrong Input entered or invalid Currency"}
