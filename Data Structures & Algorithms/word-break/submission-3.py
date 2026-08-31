class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i== len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if len(s)<i+len(word):
                    continue
                if s[i: i+ len(word)] == word:
                    res = dfs(i+len(word))
                    if res:
                        return True
            memo[i] = False

            return False
        return dfs(0)