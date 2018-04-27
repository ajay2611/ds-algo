def min_coin_sum(coins, summ):
    """
    """
    MAX = 10**16
    count = [MAX] * (summ + 1)

    for i in range(len(coins)):
        for j in range(summ + 1):
            if coins[i] <= j:
                temp = count[count[i] - j]
                if temp + 1 < count[i]:
                	count[i] = temp + 1

    return count[summ]


if __name__ == "__main__":
    n = [2, 5, 3, 6]
    c = 10
    print(min_coin_sum(n, c))
