"""Lab 02.04 - Copy Stack"""

class ArrayStack:
    """Stack Command"""
    def __init__(self):
        """Create Stack"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """pick top of Stack"""
        self.size -= 1
        if len(self.data):
            return self.data.pop(-1)
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """Check Stack wa empty mai"""
        if len(self.data):
            return False
        else:
            return True

    def get_stack_top(self):
        """return top of Stack"""
        if len(self.data):
            return self.data[-1]
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def get_size(self):
        """return size of Stack"""
        return len(self.data)

    def print_stack(self):
        """print"""
        print(self.data)

def copy_stack(stack1, stack2):
    """-"""
    stack3 = ArrayStack()
    while not stack2.is_empty():
        stack2.pop()
    for _ in range(stack1.get_size()):
        stack3.push(stack1.pop())
    for _ in range(stack3.get_size()):
        var = stack3.pop()
        stack1.push(var)
        stack2.push(var)


def main():
    """-"""
    def print_status():
        """Print all stacks"""
        print("This is stack 1 (%d): " % stack1.get_size(), end='')
        stack1.print_stack()
        print("This is stack 2 (%d): " % stack2.get_size(), end='')
        stack2.print_stack()
        print("This is stack 3 (%d): " % stack3.get_size(), end='')
        stack3.print_stack()
        print("This is stack 4 (%d): " % stack4.get_size(), end='')
        stack4.print_stack()
        print()

    stack1 = ArrayStack()
    stack2 = ArrayStack()

    stack3 = ArrayStack()
    stack4 = ArrayStack()

    # เพิ่มข้อมูลใน Stack1
    for _ in range(int(input())):
        stack1.push(input())

    # เพิ่มข้อมูลใน Stack2
    for _ in range(int(input())):
        stack2.push(input())

    temp1, temp2, temp3, temp4 = id(stack1), id(
        stack2), id(stack3), id(stack4)

    print("Copy Stack 2 to Stack 4")
    copy_stack(stack2, stack4)
    print_status()

    print("Copy Stack 1 to Stack 3")
    copy_stack(stack1, stack3)
    stack1.push("A")
    print_status()

    print("Copy Stack 2 to Stack 1")
    copy_stack(stack2, stack1)
    stack2.push("B")
    print_status()

    print("Copy Stack 3 to Stack 2")
    copy_stack(stack3, stack2)
    stack3.push("C")
    print("Copy Stack 1 to Stack 3")
    copy_stack(stack1, stack3)
    stack1.push("D")
    print("Copy Stack 2 to Stack 4")
    copy_stack(stack2, stack4)
    stack2.push("E")
    print_status()

    print(temp1 == id(stack1), temp2 == id(stack2), \
    temp3 == id(stack3), temp4 == id(stack4))

main()
