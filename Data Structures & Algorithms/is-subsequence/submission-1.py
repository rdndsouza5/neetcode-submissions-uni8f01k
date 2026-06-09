class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        i, j = 0, 0

        while j< len(t) and i < len(s):
            if s[i]!= t[j]:
                j+=1
                continue
            else:
                i+=1
                j+=1

        return i ==len(s)