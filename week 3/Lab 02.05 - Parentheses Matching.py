"""Lab 02.05 - Parentheses Matching"""

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

def is_parentheses_matching(expression):
    """main"""
    stack = ArrayStack()
    boolean = True
    for var in expression:
        if var == "(":
            stack.push(var)
        elif var == ")":
            check = stack.pop()
            if check == None:
                boolean = False
                break
    if not stack.is_empty():
        boolean = False

    if boolean:
        print("Parentheses in", expression, "are matched")
    else:
        print("Parentheses in", expression, "are unmatched")
    return boolean

def main(expression):
    """-"""
    print(is_parentheses_matching(expression))

main(input())
