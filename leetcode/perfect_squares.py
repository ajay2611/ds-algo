"""
https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""


class Solution:

    def numSquares(self, n: int) -> int:
        arr = [n] * (n + 1)
        if n <= 3:
            return n

        for _ in range(4):
            arr[_] = _

        for i in range(4, n + 1):
            for j in range(int(i ** 0.5), 0, -1):
                arr[i] = min(arr[i], 1 + arr[i - j * j])
                if arr[i] <= 2:
                    break

        return arr[-1]


if __name__ == '__main__':
    n = 12
    res = Solution().numSquares(n)
    print(res)
