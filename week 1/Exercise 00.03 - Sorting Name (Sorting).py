"""Exercise 00.03 - Sorting Name"""

def main(lst):
    """-"""
    for i in range(len(lst)):
        noi = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[noi]:
                noi = j
        lst[i], lst[noi] = lst[noi], lst[i]
    print(*lst, sep='\n')

main([input() for _ in range(int(input()))])
