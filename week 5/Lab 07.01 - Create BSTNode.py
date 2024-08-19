"""Lab 07.01 - Create BSTNode.py"""

class BSTNode:
    """-"""
    def __init__(self, data):
        """-"""
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        """-"""
        return self.data

    def set_data(self, data):
        """-"""
        self.data = data

    def get_left(self):
        """-"""
        return self.left

    def set_left(self, data):
        """-"""
        self.left = data

    def get_right(self):
        """-"""
        return self.right

    def set_right(self, data):
        """-"""
        self.right = data

def main():
    """-"""
    pnew = BSTNode(int(input()))
    print(pnew.get_data(), pnew.get_left(), pnew.get_right(), end=" ")

main()
