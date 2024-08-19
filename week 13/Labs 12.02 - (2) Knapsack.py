"""Labs 12.02 - (2) Knapsack.py"""
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

def knapsack(itemlist, amount):
    """-"""
    valueb = 0
    check = True
    backpack = []
    print("Knapsack Size: %.01f kg" % amount)
    print("===============================")
    while check:
        mcost = -1
        check = False
        if itemlist == []:
            break
        for num in range(len(itemlist)):
            if mcost == -1 or itemlist[num].get_cost() > itemlist[mcost].get_cost():
                mcost = num
        if amount - itemlist[mcost].get_weight() >= 0:
            backpack.append(itemlist[mcost])
            check = True
            amount -= itemlist[mcost].get_weight()
            valueb += itemlist[mcost].get_price()
            itemlist.pop(mcost)
        if amount == 0:
            check = False
    for buy in backpack:
        print(buy.get_all())
    print("Total: %d THB" % valueb)

def main():
    """Test area"""
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()