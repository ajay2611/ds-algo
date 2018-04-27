# Complete the function below.

def numberOfPaths(a):
    MOD = 10**9 + 7
    ans = 0
    for i, row in enumerate(a):
        for j, val in enumerate(row):
            if i==0 and j==0:
                continue
            elif i==0:
                a[i][j] = (a[i][j] and a[i][j-1])%MOD
            elif j==0:
                a[i][j] = (a[i][j] and a[i-1][j])%MOD
            else:
                a[i][j] = (a[i][j] and (a[i-1][j]+ a[i][j-1]))%MOD
    return a[-1][-1]%MOD

if __name__ == '__main__':
    a = [[1,1,1], [1,1,1], [1,1,1]]
    numberOfPaths(a)

