def lcs_dp(x, y):
    """
    :param x: string 1
    :param y: string 2
    :return: longest common subsequence between x and y using DP
    """
    m = len(x)
    n = len(y)
    lcs = [[None] * (n + 1) for i in range(m + 1)]

    # filling lcs matrix using bottom up approach
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    lcs_length = lcs[m][n]
    # string to store longest common subsequence (lcs)
    lcs_string = [''] * lcs_length

    i = m
    j = n
    while i > 0 and j > 0:
        # if characters are same, then they are part of lcs
        if x[i - 1] == y[j - 1]:
            lcs_string[lcs_length - 1] = x[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            # deciding whether to move up or down
            i -= 1
        else:
            j -= 1

    return "".join(lcs_string), lcs[m][n]


def longest_palindromic_sub(s):
    """
    :param s: string for which longest palindromic subsequence is to be found
    :return: longest palindromic subsequence and its length
    """
    rev = "".join(reversed(s))
    return lcs_dp(s, rev)

if __name__ == '__main__':
    s = "BBABCBCAB"
    sub, length = longest_palindromic_sub(s)
    print('"{}" of length {}'.format(sub, length))
