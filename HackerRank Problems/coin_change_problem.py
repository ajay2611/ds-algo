
def get_ways(coins, summ):
    """
    Desc: finding number of ways of making change for a particular number of units (c)
    using the given types of coins (n)
    :param coins - list of coins
    :param summ - required change to be returned to customer
    :return - number of ways of getting summ
    """
    # to store possible sum of all values upto sum
    count = [0] * (summ + 1)
    # if there is no money, i.e. coins
    count[0] = 1
    # find sum considering each denomination of coin
    for i in range(len(coins)):
        # run inner loops for sum j which are bigger than current coin i
        for j in range(coins[i], summ+1):
            count[j] += count[j - coins[i]]

    return count[summ]


if __name__ == "__main__":
    n = [2, 5, 3, 6]
    c = 10
    print(get_ways(n,c))