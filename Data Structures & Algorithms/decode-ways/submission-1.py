class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(i):
            if i  == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            res = dfs(i+1)
            memo[i+1]= res
            if i <(len(s))-1 :
                if (s[i] == '1' or (s[i]=='2' and s[i+1]<'7')):
                    memo[i+2]=  dfs(i+2)
                    res+= memo[i+2]
            return res

        return dfs(0)