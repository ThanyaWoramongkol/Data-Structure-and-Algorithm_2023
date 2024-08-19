"""Lab 09.02 - isIntersect(A,B,C)"""
from json import loads
def intersect(lst):
    """-"""
    for i in lst[0]:
        if i in lst[1] and i in lst[2]:
            return True
    return False
print(intersect([loads(input()) for _ in range(3)]))
