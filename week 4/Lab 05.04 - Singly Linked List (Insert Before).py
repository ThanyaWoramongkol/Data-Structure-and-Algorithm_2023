"""Lab 05.04 - Singly Linked List (Insert Before)"""

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
        self.count += 1


    def insert_front(self, data):
        """-"""
        pnew = DataNode(data)
        pnew.set_next(self.head)
        self.head = pnew
        self.count += 1

    def insert_before(self, node, data):
        """-"""
        pnew = DataNode(data)
        position = self.head
        prev = None
        if position != None and position.get_data() == node:
            self.insert_front(data)
        else:
            while position != None:
                if position.get_data() == node:
                    prev.set_next(pnew)
                    pnew.set_next(position)
                    break
                prev = position
                position = position.get_next()
            if position == None:
                print("Cannot insert, {} does not exist.".format(node))

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
    """_"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()


main()
