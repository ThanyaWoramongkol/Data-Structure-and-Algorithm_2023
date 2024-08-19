"""Lab 02.03 - Student Groups"""

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

def main(group, jumnuan):
    """-"""
    stack = ArrayStack()
    data = [[] for _ in range(group)]
    for _ in range(jumnuan):
        stack.push(input())
 
    num = 0
    while not stack.is_empty():
        data[num % len(data)].append(stack.pop())
        num += 1
 
    for i in range(group):
        print("Group %d: " % (i+1), end="")
        print(', '.join(data[i % len(data)]))
main(int(input()), int(input()))