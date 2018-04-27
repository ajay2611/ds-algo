def find_max_profit(a):
    profit = 0
    if not a:
        return profit

    # initializing maximum so far as last value in price array
    max_so_far = a[-1]
    # traverse array from back side and find maximum so far
    # and calculate profit for that index
    for i in range(len(a) - 2, -1, -1):
        max_so_far = max(max_so_far, a[i])
        profit += max_so_far - a[i]

    return profit


if __name__ == '__main__':
    a = [2, 1, 3, 40, 5, 8]
    print(find_max_profit(a))
