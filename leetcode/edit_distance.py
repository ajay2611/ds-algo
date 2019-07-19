"""
https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution:

    def minDistance_recursive(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        else:
            return 1 + min(self.minDistance(word1, word2[:-1]),
                           self.minDistance(word1[:-1], word2),
                           self.minDistance(word1[:-1], word2[:-1]))

    def minDistance(self, word1, word2):
        """
        DP based solution
        """
        dp = [[0 for i in range(len(word2) + 1)]
              for j in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],
                                       dp[i - 1][j],
                                       dp[i - 1][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "ajay"
    word2 = "ajax"
    print(Solution().minDistance(word1, word2))
