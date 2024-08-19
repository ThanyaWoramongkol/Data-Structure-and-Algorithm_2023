"""Lab 09.01 - Summation (Type 1)"""
# from time import time

def summation(number):
    """-"""
    result = 0
    for i in range(number):
        result += i+1
    return result
print(summation(int(input())))

