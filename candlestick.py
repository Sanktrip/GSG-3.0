

class Candlestick:
    open_price = 0
    close_price = 0
    high_price = 0
    low_price = 0
    quote_volume = 0

    def __init__(self, open_price, close_price, high_price, low_price, quote_volume):
        self.close_price = float(close_price)
        self.open_price = float(open_price)
        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.quote_volume = float(quote_volume)
        
    def __str__(self) -> str:
        string = "o_p: " + str(self.open_price)
        string += "\nc_p: " + str(self.close_price)
        string += "\nh_p: " + str(self.high_price)
        string += "\nl_p: " + str(self.low_price)
        string += "\nq_v: " + str(self.quote_volume)
        return string