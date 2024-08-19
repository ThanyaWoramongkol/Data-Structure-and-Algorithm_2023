"""Exercise 01.02 - Laew Tae App V.1"""

class Laeotaeapp:
    """-"""
    def __init__(self):
        """-"""
        self.food_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]

        self.random_foods()
        self.list_foods()

    def random_foods(self):
        """-"""
        self.food_list.sort()

    def list_foods(self):
        """-"""
        print(self.food_list)

Laeotaeapp()

