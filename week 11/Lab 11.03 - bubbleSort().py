"""Lab 11.03 - bubbleSort().py"""
from json import loads
def bubblezort(lst, last):
    """-"""
    current = 0
    counter = 0
    sorted_ = False
    while not sorted_ and current <= last:
        walker = last
        sorted_ = True
        while walker > current:
            counter += 1
            if lst[walker] < lst[walker - 1]:
                sorted_ = False
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
            walker -= 1
        current += 1
        # last -= 1

        print(lst)
    print("Comparison times:", counter)

bubblezort(loads(input()), int(input()))
