
class DataNode:
    """-"""
    def __init__(self, data):
        """-"""
        self.data = data
        self.next = None

    def get_data(self):
        """-"""
        return self.data

    def set_data(self, data):
        """-"""
        self.data = data

    def get_next(self):
        """-"""
        return self.next

    def set_next(self, nexts):
        """-"""
        self.next = nexts

def main(name):
    """-"""
    print(name)
    print(None)
main(input())
