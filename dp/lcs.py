# Longest Common Subsequence


def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1)
    else:
        return max(lcs(x, y, m - 1, n), lcs(x, y, m, n - 1))


def lcs_dp(x, y):
    m = len(x)
    n = len(y)
    lcs = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[m][n]

if __name__ == '__main__':
    s1 = "ajay singh"
    s2 = "jay sin goh"
    length = lcs(s1, s2, len(s1), len(s2))
    length_dp = lcs_dp(s1, s2)
    print(length, length_dp)
