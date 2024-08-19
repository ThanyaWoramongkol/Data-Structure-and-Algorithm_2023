"""Lab 01.04 - Rectangle"""

class Rectangle:
    """-"""
    def __init__(self, height, width):
        """setting"""
        self.height = height
        self.width = width

    def calculate_area(self):
        """h*w"""
        return self.height * self.width

    def calculate_perimeter(self):
        """(h+w) * 2"""
        return (self.height + self.width) * 2

def main():
    """-"""
    rectangle = Rectangle(float(input()), float(input()))
    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)

main()
