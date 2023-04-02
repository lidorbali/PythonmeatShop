class Product(object):
    """
     list of objects
    : Action to perform:
    Connecting quantities of the same object
    Subtraction subtractors of the same object
    Printing a single object or multiple objects in a list
    """

    def __init__(self, list):
        self.__meat_type = list[0]
        self.__meat_product = list[1]
        self.__amount = float(list[4])
        self.__price = float(list[3])
        self.__condition = list[2]

    def set_amount(self, amount):  # set an new amount
        self.__amount = amount

    def set_price(self, price):  # set new price
        self.__price = price

    def get_type(self):
        return self.__meat_type

    def get_price(self):
        return self.__price

    def get_amount(self):
        return self.__amount

    def get_name(self):
        return self.__meat_product

    def get_condition(self):
        return self.__condition

    def add(self, amount):
        self.__amount += amount
        return self

    def sub(self, amount):
        self.__amount -= amount
        return self

    def __str__(self):
        return f"סוג :{self.__meat_product} {self.__condition} כמות :{self.__amount}קג מחיר לקג : {self.__price}שקל"
