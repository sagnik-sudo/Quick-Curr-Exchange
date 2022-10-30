from typing import Union
from fastapi import FastAPI
from src.currency_lister import CurrencyList
from src.currency_converter import CurrencyConverter

DESCRIPTION = """
This is a simple open source application that allows you to fetch currency conversion data.
You can just provide a two currencies and get the convertion as output.
For suggestions and contributions, please visit [github.com/sagnik-sudo/Quick-Curr-Exchange](https://github.com/sagnik-sudo/Quick-Curr-Exchange/issues)
If you like my work, please star it on [github.com/sagnik-sudo/Quick-Curr-Exchange](https://github.com/sagnik-sudo/Quick-Curr-Exchange)
"""

app = FastAPI(
    title="Quick Curr Exchange",
    description=DESCRIPTION,
    version="Beta",
    docs_url="/currencies",
    redoc_url="/currencies/redoc",
    contact={
        "name": "Developer - Sagnik Das",
        "email": "sagnikdas2305@gmail.com",
    },
)


@app.get("/supportedcurrencies",
         tags=["Currency Conversion"],
         name="Fetches list of supported Currencies")
async def get_currencies():
    """
    Get the list of currencies supported by this application
    """
    currobj = CurrencyList()
    output = currobj.fetch()
    return output


@app.post("/convert_live", tags=["Currency Conversion"],
          name="Convert a amount from local currency to another currency (Live)")
async def convert(from_currency, to_currency, amount, date: Union[str, None] = None):
    """
    Convert a local currency amount to another currency amount
    """
    currobj = CurrencyConverter()
    output = currobj.convert(from_currency, to_currency, amount, date)
    return output
