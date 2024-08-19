"""Exercise 01.04 - Bangna Trad"""

def road(kilogram):
    """-"""
    if kilogram < 0 or kilogram > 58.855:
        print("InValid")
    elif kilogram > 52.900:
        print("Chon Buri")
    elif kilogram > 35.477:
        print("Chachoengsao")
    elif kilogram > 5.032:
        print("Samut Prakarn")
    else:
        print("Bangkok")

road(float(input()))
