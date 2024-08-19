"""Lab 09.03 - Calculator"""

def calculator(number):
    """-"""
    count = 0
    if number != 1:
        for i in range(number):
            count += len(str(i+1)) + 1
    else:
        count += 1
    print(count)
calculator(int(input()))
