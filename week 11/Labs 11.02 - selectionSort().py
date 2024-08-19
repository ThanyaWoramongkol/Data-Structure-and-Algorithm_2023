"""Labs 11.02 - selectionSort().py"""
from json import loads
def selectionzort(lst, last):
    """-"""
    current = 0
    counter = 0
    while current < last:
        smallest = current
        walker = current + 1

        while walker <= last:
            counter += 1
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1

        lst[current], lst[smallest] = lst[smallest], lst[current]
        current += 1

        # last -= 1
        print(lst)
    print("Comparison times:", counter)
selectionzort(loads(input()), int(input()))
