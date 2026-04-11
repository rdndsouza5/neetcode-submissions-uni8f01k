class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a=list(s)
        for i in t:
            if i not in a:
                return False
            a.remove(i)
        return True