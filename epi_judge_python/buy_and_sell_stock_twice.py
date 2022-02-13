from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_total_profit, min_price_so_far, max_price_so_far = 0.0, float('inf'), float('-inf')
    first_buy_sell_profit = [0.0] * len(prices)
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profit[i] = max_total_profit
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profit[i]
        )
    return max_total_profit

# avg/med: 251 us/30 us
# def buy_and_sell_stock_twice(prices: List[float]) -> float:
#     max_total_profit, min_price_so_far, max_price_so_far = 0.0, float('inf'), float('-inf')
#     first_buy_sell_profit = [0.0] * len(prices)
#     for i, price in enumerate(prices):
#         min_price_so_far = min(min_price_so_far, price)
#         max_total_profit = max(max_total_profit, price - min_price_so_far)
#         first_buy_sell_profit[i] = max_total_profit
#     for i, price in reversed(list(enumerate(prices[1:], 1))):
#         max_price_so_far = max(max_price_so_far, price)
#         max_total_profit = max(
#             max_total_profit,
#             max_price_so_far - price + first_buy_sell_profit[i]
#         )
#     return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
