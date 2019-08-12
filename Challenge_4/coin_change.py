def least_coins(coins, n):
    change_amount = 0
    coins_returned = []

    for coin in coins[::-1]:
        while n - change_amount >= coin:
            change_amount += coin
            coins_returned.append(coin)

    return coins_returned


# def least_coins_recursively(coins, n, returned=[]):

#     if n == 0:
#         return 0

#     if n in coins:
#         return n

#     returned = []
#     for coin in coins[::-1]:
#         returned.append(least_coins_recursively([coin], ))
if __name__ == '__main__':
    coins = [1, 3, 5, 7]

    print(least_coins(coins, 19))
