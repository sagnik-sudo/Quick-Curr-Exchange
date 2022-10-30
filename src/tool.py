class QuickTool:
    """Miscellaneous tools useful for this application"""

    def __init__(self):
        pass

    def prepare_url(self, fr_curr, to_curr, amount):
        """Returns prepared url for the given combination"""
        return f"https://api.exchangerate.host/convert?from={fr_curr}&to={to_curr}&amount={amount}"

    def prepare_url_withdate(self, fr_curr, to_curr, amount, date):
        """Returns prepared url for the given combination with date"""
        return f"https://api.exchangerate.host/convert?from={fr_curr}&to={to_curr}&amount={amount}&date={date}"

    def prepare_url_historical(self, fr_curr, date):
        """Returns prepared url for a historical date"""
        return f"https://api.exchangerate.host/{date}?base={fr_curr}"

    def prepare_url_timeseries(self, start_date, end_date, fr_curr, to_curr):
        """Returns prepared url for a timeseries of currency amount"""
        return f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&base={fr_curr}&symbols={to_curr}"
