import requests
from src.tool import QuickTool


class CurrencyConverter:
    """
    This class is used to convert currency
    """

    def __init__(self):
        """
        Constructor
        """
        self.url = 'https://api.exchangerate.host/convert'
        self.prepared_url = ''
        self.result = {}
        self.tool = QuickTool()

    def convert(self, fr_curr, to_curr, amount, date):
        """
        This function is used to convert currency
        """
        if date == None:
            self.prepared_url = self.tool.prepare_url(fr_curr, to_curr, amount)
            response = requests.get(self.prepared_url)
            if response.status_code == 200:
                self.result = response.json()
        else:
            self.prepared_url = self.tool.prepare_url_withdate(
                fr_curr, to_curr, amount, date)
            response = requests.get(self.prepared_url)
            if response.status_code == 200:
                self.result = response.json()
            else:
                raise Exception(response.status_code, {
                                "Error:": "Failed to convert"})
        output = {"Source": fr_curr, "Target": to_curr,
                  "SourceAmount": f"{fr_curr} {amount}",
                  "TargetAmount": f"{to_curr} {self.result['result']}",
                  "ConversionDate": self.result['date'],
                  "Result": self.result['result'], "UnitRate": {f"{fr_curr} to {to_curr}": self.result['info']['rate']}}
        if output['Result'] is None:
            raise Exception(response.status_code, {
                "Error:": "Incorrect input format"})
        else:
            return output
