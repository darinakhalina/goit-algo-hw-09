def find_coins_greedy(amount, coins):
    result = {}
    coins.sort(reverse=True)

    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount %= coin

    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113

find_coins_greedy_result = find_coins_greedy(amount, coins)
print("Результат find_coins_greedy", find_coins_greedy_result)
