class Computer:
    def __init__(self):
        self._maxprice = 900
    
    def sell(self):
        print("Selling price: {}".format(self._maxprice))
    
    def set_max_price(self, price):
        self._maxprice = price

# Creating an object of the Computer class
c = Computer()
c.sell()  # Prints the initial price

# Updating the max price
c.set_max_price(1000)
c.sell()  # Prints the updated price
