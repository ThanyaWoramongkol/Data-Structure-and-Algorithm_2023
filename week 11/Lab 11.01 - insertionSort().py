"""Lab 11.01 - insertionSort().py"""
from json import loads
def insertionzort(lst, last):
    """-"""
    counter = 0
    current = 1

    for index in range(current, len(lst)):
        if not last:
            break
        key = lst[index]
        walker = index-1
        while walker >= 0:
            counter += 1
            if key >= lst[walker]:
                break
            else:
                lst[walker+1] = lst[walker]
                walker -= 1

        lst[walker+1] = key

        last -= 1

        print(lst)
    print("Comparison times: %d" % counter)

insertionzort(loads(input()), int(input()))
