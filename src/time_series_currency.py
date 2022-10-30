import requests
import pandas as pd
from src.tool import QuickTool


class TimeSeries:
    """Returns a list of time series for the given pair of currencies and dates."""

    def __init__(self, from_date, to_date, fr_curr, to_curr):
        self.from_date = from_date
        self.to_date = to_date
        self.fr_curr = fr_curr
        self.to_curr = to_curr
        self.prepared_url = ""
        self.tool = QuickTool()

    def fetch(self):
        """Returns time series for given pair of currencies"""
        self.prepared_url = self.tool.prepare_url_timeseries(
            self.from_date, self.to_date, self.fr_curr, self.to_curr)
        response = requests.get(self.prepared_url)
        if response.status_code == 200:
            response_dict = response.json()
            output_pd = pd.DataFrame.from_dict(
                response_dict['rates']).transpose()
            rates = output_pd.to_dict()[self.to_curr]
            aggregation = output_pd.describe().to_dict()[self.to_curr]
            return {"SourceCurrency": self.fr_curr, "TargetCurrency": self.to_curr,
                    "FromDate": self.from_date, "ToDate": self.to_date, 
                    "ExchangeRateAnalysis": aggregation, "ExchangeRatesDay": rates}
        else:
            raise Exception(response.status_code, {
                "Error:": "Failed to get historical rates"})
