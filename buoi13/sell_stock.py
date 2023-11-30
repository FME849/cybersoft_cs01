lst_price = [7, 1, 5, 3, 6, 4]

def max_diff(lst:list[int]):
    max_diff = None
    for idx, price in enumerate(lst):
        for j in range(idx + 1, len(lst)):
            diff = lst[j] - price
            if max_diff == None or max_diff < diff:
                max_diff = diff
    return max_diff

def max_profit_v2(prices:list[int]):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    return max_profit


print(max_profit_v2(lst_price))

