class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word = set(dictionary)
        hs = {}
        def dfs(i):
            if i == len(s):
                return 0
            
            if i in hs:
                return hs[i]

            res = 1 + dfs(i+1)   #skip current char

            for j in range(i, len(s)):
                if s[i:j+1] in word:
                    res= min(res, dfs(j+1))
            hs[i] = res
            return res
        return dfs(0)