"""Lab 01.06 - Elevator"""

class Elevator:
    """-"""
    def __init__(self, max_floor):
        """-"""
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """-"""
        if floor > self.max_floor:
            print("Invalid Floor!")
        else:
            self.current_floor = floor

    def report_current_floor(self):
        """-"""
        print(self.current_floor)

def main():
    """-"""
    elevator = Elevator(int(input()))
    while True:
        level = input()
        if level == "Done":
            elevator.report_current_floor()
            break
        else:
            elevator.go_to_floor(int(level))

main()
