"""Lab 07.02 - Binary Search Tree (Preorder, Insert)"""

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
        pass

    def find_min(self):
        """-"""
        pass

    def find_max(self):
        """-"""
        pass

    def is_empty(self):
        """-"""
        pass

    def preorder(self, root):
        """-"""
        if root != None:
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

    def inorder(self, root):
        """-"""
        if root != None:
            self.preorder(root.get_left())
            print("->", root.get_data(), end=" ")
            self.inorder(root.get_right())

    def postorder(self, root):
        """-"""
        if root != None:
            self.preorder(root.get_left())
            self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")

    def traverse(self):
        """-"""
        pass

def main():
    """_"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder(my_bst.get_root())
main()
