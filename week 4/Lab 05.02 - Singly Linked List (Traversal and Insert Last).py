"""Lab 04.01 - Create DataNode"""

class DataNode:
    """-"""
    def __init__(self, data=None):
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

class SinglyLinkedList:
    """-"""
    def __init__(self):
        """-"""
        self.count = 0
        self.head = None

    def insert_last(self, data):
        """-"""
        pnew = DataNode(data)
        if self.head == None:
            self.head = pnew
        else:
            start = self.head
            while start.get_next() != None:
                start = start.get_next()
            start.set_next(pnew)


    def insert_front(self, data):
        """-"""
        pass

    def insert_before(self, node, data):
        """-"""
        pass

    def delete(self, data):
        """-"""
        pass

    def traverse(self):
        """-"""
        if self.head != None:
            position = self.head
            while position != None:
                print(position.get_data(), ("-> " if position.get_next() != None else ""), end="")
                position = position.get_next()
        else:
            print("This is an empty list.")

def main():
    """-"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()
