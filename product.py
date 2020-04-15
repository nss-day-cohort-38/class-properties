# class Product():

#     def __init__(self):
#         self.price = 0
#         self.title = ""
#         self.description = ""


class Product():
    def __init__(self, title):
        self.__title = title
        self.description = ""

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        try:
            return self.__amount
        except AttributeError:
            return 0
    
    @price.setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__amount = new_price
        else:
            raise TypeError("Please provide a floating point value for the price")
    

# instance of Product class
kite = Product("Kite")
kite.price = 14.99

# If the user tries to set price to a value that isn't type float, the code will throw an error
# kite.price = "$14.99"

# User cannot change the value of kite.title after it is initialized. The below code will throw an error
# kite.title = "A red kite"

