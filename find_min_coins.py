def find_min_coins(amount, coins):
    max_coins = amount // min(coins)

    min_coins = [max_coins] * (amount + 1)
    min_coins[0] = 0

    selected_coins = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                selected_coins[i] = coin

    result = {}
    while amount > 0:
        coin = selected_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113

find_min_coins_result = find_min_coins(amount, coins)
print("Результат find_min_coins", find_min_coins_result)
