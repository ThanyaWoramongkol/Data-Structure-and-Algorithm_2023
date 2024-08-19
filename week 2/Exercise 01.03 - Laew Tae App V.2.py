"""Exercise 01.02 - Laew Tae App V.1"""

class Laeotaeapp:
    """-"""
    def __init__(self, count):
        """-"""
        self.food_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.count = count

        self.random_foods()

    def random_foods(self):
        """-"""
        self.count += 1

    def list_foods(self):
        """-"""
        self.food_list.sort()
        print(self.food_list)

    def add_food_item(self, name):
        """-"""
        self.food_list.append(name)

def main():
    """-"""
    app = Laeotaeapp(0)
    for _ in range(int(input())):
        app.add_food_item(input())
    app.list_foods()

main()
