def _backtrack(s, word_dict, temp, final):
    if not s:
        final.append(temp.strip())
        
    for i in range(1, len(s)+1):
        if s[:i] in word_dict:
            _backtrack(s[i:], word_dict, temp + s[:i] + " ", final)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        final = []
        _backtrack(s, wordDict, "", final)
        return final


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]

    print(Solution().wordBreak(s, wordDict))