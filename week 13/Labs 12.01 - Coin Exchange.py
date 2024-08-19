"""Labs 12.01 - Coin Exchange.py"""
from json import loads
def convert_key(data):
    """-"""
    return {int(k): v for k, v in data.items()}

def main(money, dic):
    """-"""
    change = 0
    counter = {}

    final_money = money
    coins = [10, 5, 2, 1]
    data = convert_key(dic)

    for rian in coins:
        needed = money // rian
        jumnuan = data[rian]
        if jumnuan < needed:
            needed = jumnuan
        money -= rian * needed
        counter[rian] = needed

    print("Amount:", final_money)
    if money > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for num in coins:
            print("  %d baht = %d coins" % (num, counter[num]))
            change += counter[num]
        print("Number of coins:", change)

main(int(input()), loads(input()))
