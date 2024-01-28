import timeit
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def measure_time(algorithm, amount, coins):
    return timeit.timeit(lambda: algorithm(amount, coins), number=5)


coins_test_1 = [50, 25, 10, 5, 2, 1]
amount_test_1 = 113

coins_test_2 = [50, 25, 10, 5, 2, 1]
amount_test_2 = 23313

coins_test_3 = [10, 5, 2, 1]
amount_test_3 = 97933

coins_test_4 = [10, 5, 2, 1]
amount_test_4 = 45789537

time_min_coins_test_1 = measure_time(find_min_coins, amount_test_1, coins_test_1)
time_greedy_test_1 = measure_time(find_coins_greedy, amount_test_1, coins_test_1)

time_min_coins_test_2 = measure_time(find_min_coins, amount_test_2, coins_test_2)
time_greedy_test_2 = measure_time(find_coins_greedy, amount_test_2, coins_test_2)

time_min_coins_test_3 = measure_time(find_min_coins, amount_test_3, coins_test_3)
time_greedy_test_3 = measure_time(find_coins_greedy, amount_test_3, coins_test_3)

time_min_coins_test_4 = measure_time(find_min_coins, amount_test_4, coins_test_4)
time_greedy_test_4 = measure_time(find_coins_greedy, amount_test_4, coins_test_4)

print(
    f"{'| Алгоритм': <20} | {'Тест 1': <20} | {' Тест 2': <20} | {'Тест 3': <20} | {'Тест 4': <20}"
)
print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")
print(
    f"{'| find_min_coins': <20} | {time_min_coins_test_1:<20.8f} | {time_min_coins_test_2:<20.8f} | {time_min_coins_test_3:<20.8f} | {time_min_coins_test_4:<20.8f} "
)
print(
    f"{'| find_coins_greedy': <20} | {time_greedy_test_1:<20.8f} | {time_greedy_test_2:<20.8f} | {time_greedy_test_3:<20.8f} | {time_greedy_test_4:<20.8f} "
)
