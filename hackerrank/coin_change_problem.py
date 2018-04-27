def get_ways(coins, summ):
    """
    Desc: finding number of ways of making change for a particular number of units (c)
    using the given types of coins (n)
    :param coins - list of coins
    :param summ - required change to be returned to customer
    :return - number of ways of getting summ
    """
    # to store possible sum of all values upto sum
    count = [1] + [0] * (summ)
    # find sum considering each denomination of coin
    for c in coins:
        # run inner loops for sum j which are bigger than current coin i
        for i in range(summ + 1):
            if i + c <= summ:
                count[i + c] += count[i]

    return count[-1]


if __name__ == "__main__":
    n = [2, 5, 3, 6]
    c = 10
    print(get_ways(n, c))
