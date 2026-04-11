class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        mapp = {}

        for i in range(len(s)):
            mapp[s[i]] = mapp.get(s[i],0)+1
            mapp[t[i]] = mapp.get(t[i],0)-1

        for k,v in mapp.items():
            if v !=0:
                return False
        return True