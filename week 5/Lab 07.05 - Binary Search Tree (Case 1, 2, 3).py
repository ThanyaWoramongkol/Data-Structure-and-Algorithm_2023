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

class BST:
    """-"""
    def __init__(self):
        """-"""
        self.root = None

    def get_root(self):
        """-"""
        return self.root

    def set_root(self, root):
        """-"""
        self.root = root

    def insert(self, data):
        """-"""
        pnew = BSTNode(data)
        if self.root != None:
            prev = None
            start = self.root

            while start != None:
                prev = start
                if data < start.get_data():
                    start = start.get_left()
                else:
                    start = start.get_right()
            if data < prev.get_data():
                prev.set_left(pnew)
            else:
                prev.set_right(pnew)
        else:
            self.root = pnew

    def delete(self, data):
        """-"""
        if self.root != None:
            start = self.root
            prev = None
            while start.get_data() != data:
                prev = start
                if data < start.get_data():
                    start = start.get_left()
                else:
                    start = start.get_right()
                if start == None:
                    print("Delete Error, %s is not found in Binary Search Tree." % data)
                    return

            def delete_case1(start, prev):
                """-"""
                if prev == None:
                    self.root = None
                elif data < prev.get_data():
                    prev.set_left(None)
                else:
                    prev.set_right(None)
                del start

            def delete_case2(start, prev):
                """-"""
                if prev == None:
                    self.root = start.get_left()
                elif data < prev.get_data():
                    prev.set_left(start.get_left())
                else:
                    prev.set_right(start.get_left())
                del start

            def delete_case3(start, prev):
                """-"""
                if prev == None:
                    self.root = start.get_right()
                elif data < prev.get_data():
                    prev.set_left(start.get_right())
                else:
                    prev.set_right(start.get_right())
                del start

            # def delete_case4(start):
            #     """-"""
            #     delete = start
            #     maxi = start.get_left()
            #     while maxi.get_right() != None:
            #         maxi = maxi.get_right()
            #     self.delete(maxi.get_data())
            #     delete.set_data(maxi.get_data())

            if start.get_left() == None and start.get_right() == None:
                delete_case1(start, prev)
            elif start.get_left() != None and start.get_right() == None:
                delete_case2(start, prev)
            elif start.get_left() == None and start.get_right() != None:
                delete_case3(start, prev)
            # else:
            #     delete_case4(start)

        else:
            print("Delete Error, %s is not found in Binary Search Tree." % data)

    def find_min(self):
        """-"""
        if self.root == None:
            return None
        start = self.root
        prev = None
        while start != None:
            prev = start
            start = start.get_left()
        return prev.get_data()

    def find_max(self):
        """-"""
        if self.root == None:
            return None
        start = self.root
        prev = None
        while start != None:
            prev = start
            start = start.get_right()
        return prev.get_data()

    def is_empty(self):
        """-"""
        return self.root == None

    def preorder(self, root):
        """-"""
        if root != None:
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

    def inorder(self, root):
        """-"""
        if root != None:
            self.inorder(root.get_left())
            print("->", root.get_data(), end=" ")
            self.inorder(root.get_right())

    def postorder(self, root):
        """-"""
        if root != None:
            self.postorder(root.get_left())
            self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")

    def traverse(self):
        """-"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print("Preorder: ", end="")
        self.preorder(self.root)
        print("\nInorder: ", end="")
        self.inorder(self.root)
        print("\nPostorder: ", end="")
        self.postorder(self.root)

def main():
    """_"""
    my_bst = BST()
    while True:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()
