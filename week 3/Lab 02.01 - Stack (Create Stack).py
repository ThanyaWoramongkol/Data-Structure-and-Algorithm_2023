"""Lab 02.01 Stack (Create Stack)"""

class ArrayStack:
    """-"""
    def __init__(self):
        """-"""
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
    stack = ArrayStack()

    stack.push("100")
    stack.push(100)
    stack.push("3.14")
    stack.push(3.14)
    stack.push("66.4a")
    stack.push("Ackerman")

    stack.print_stack()

    print(stack.get_size())
    var = stack.pop()
    print(var)
    stack.print_stack()
    print(stack.get_size())

    while not stack.is_empty():
        print(stack.pop())

    print()
    print(stack.pop())
    print(stack.get_stack_top())
    print(var)
main()
