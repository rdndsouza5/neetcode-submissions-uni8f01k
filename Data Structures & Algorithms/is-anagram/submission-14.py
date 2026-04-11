class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = {} 
        for i in range(len(s)):
            res[s[i]] = 1+ res.get(s[i],0)
            res[t[i]] = res.get(t[i], 0 )-1
        for v in res.values():
            if v!=0:
                return False
        return True
        