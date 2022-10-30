import requests
import pandas as pd


class CurrencyList:
    """
    This class is used to get the list of currencies
    """

    def __init__(self):
        self.currencies = {}
        self.url = 'https://api.exchangerate.host/symbols'

    def fetch(self):
        """
        Fetches the list of currencies
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            self.currencies = data["symbols"]
            currencies_df = pd.DataFrame.from_dict(
                self.currencies).transpose().set_index('description')
            return currencies_df.to_dict()['code']
        else:
            raise Exception(response.status_code, "Service Down")
