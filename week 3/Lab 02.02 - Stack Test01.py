"""Lab 02.02 - Stack Test01"""

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

def main():
    """-"""
    name = ["Walter", "Skyler", "Jesse", "Saul", "Mike", "Hank", "Marie", "Kim", "Gustavo", \
    "Salamanca"]

    def print_status():
        """Print all stacks"""
        print("This is stack 1 (%d): " % stack1.get_size(), end='')
        stack1.print_stack()
        print("This is stack 2 (%d): " % stack2.get_size(), end='')
        stack2.print_stack()
        print("This is stack 3 (%d): " % stack3.get_size(), end='')
        stack3.print_stack()
        print()

    stack1 = ArrayStack()
    stack2 = ArrayStack()
    stack3 = ArrayStack()
    for i in range(len(name) // 2):
        stack1.push(name.pop())
        stack2.push(name.pop())
    print_status()

    while not stack1.is_empty() and not stack2.is_empty():
        stack3.push(stack1.get_stack_top())
        stack3.push(stack2.pop())
    print_status()

    for _ in range(stack3.get_size() + 1):
        stack3.pop()
    print_status()

    while not stack1.is_empty():
        temp = stack1.pop()
        stack2.push(temp)
        stack3.push(temp)
    print_status()

    while not stack2.is_empty():
        temp = stack2.pop()
        print(temp)
    print()
    print_status()

    while not stack3.is_empty():
        stack2.push(stack3.pop())
    print_status()

main()
