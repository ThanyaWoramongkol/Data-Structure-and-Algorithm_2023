"""Lab 01.05 - Point"""

class Point:
    """-"""
    def __init__(self, var_x, var_y):
        """-"""
        self.set_coordinates(var_x, var_y)

    def set_coordinates(self, var_x, var_y):
        """-"""
        self.var_x = var_x
        self.var_y = var_y

    def get_coordinates(self):
        """-"""
        return (self.var_x, self.var_y)

    def calculate_distance(self, other_point):
        """-"""
        return ((other_point.var_x - self.var_x)**2 + (other_point.var_y - self.var_y)**2) ** 0.5

def main():
    """-"""
    point1 = Point(float(input()), float(input()))
    point2 = Point(float(input()), float(input()))
    print("%.2f" % point1.calculate_distance(point2))
main()
