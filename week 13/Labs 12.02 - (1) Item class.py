"""Labs 12.02 - (1) Item class.py"""
from json import loads
class Item:
    """-"""
    def __init__(self, name="", price=0, weight=0.0):
        """-"""
        self.__name = str(name)
        self.__price = int(price)
        self.__weight = float(weight)

    def get_name(self):
        """return name"""
        return self.__name

    def get_price(self):
        """return price"""
        return self.__price

    def get_weight(self):
        """return weight"""
        return self.__weight

    def get_cost(self):
        """return cost"""
        return self.get_price() / self.get_weight()

    def get_all(self):
        """return name price weight"""
        return self.get_name(), "->", " %g" % self.get_weight(), "kg ->", self.get_price(), "THB"

def main():
    """-"""
    item_in = loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), "%g" % item.get_weight(), sep="\n")
main()
