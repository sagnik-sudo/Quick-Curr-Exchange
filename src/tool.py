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
