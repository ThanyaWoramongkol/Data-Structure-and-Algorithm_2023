"""Exercise 00.02 - rain? (Condition)"""

def rainy(position, before_rain):
    """480 - 240"""
    if (position == 'Outdoor' and before_rain >= 240) \
    or (position == 'Indoor' and before_rain >= 480):
        print(True)
    else:
        print(False)
rainy(input(), float(input()))
