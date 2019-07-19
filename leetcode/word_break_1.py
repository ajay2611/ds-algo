"""
https://leetcode.com/problems/word-break/
"""


class Solution:

    def wordBreak(self, s, wordDict):
        """
        Recursive solution
        """
        if not s:
            return True

        ans = False
        for idx in range(1, len(s) + 1):
            if s[:idx] in wordDict:
                ans = ans or self.wordBreak(s[idx:], wordDict)

        return ans

    def wordBreakDP(self, s, wordDict):
        """
        DP based solution
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i + 1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]

s = Solution()
res = s.wordBreak("goalspecial", ["go", "goal", "goals", "special"])
res_dp = s.wordBreakDP("goalspecial", ["go", "goal", "goals", "special"])
print(res, res_dp, res == res_dp)
