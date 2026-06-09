class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word = set(dictionary)
        hs = {}
        def dfs(i):
            if i == len(s):
                return 0
            
            if i in hs:
                return hs[i]

            hs[i+1] = dfs(i+1)   
            res = 1 + hs[i+1] #skip current char

            for j in range(i, len(s)):
                if s[i:j+1] in word:
                    hs[j+1]=dfs(j+1)
                    res= min(res, hs[j+1])
            return res
        return dfs(0)