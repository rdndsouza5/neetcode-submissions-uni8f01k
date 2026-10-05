class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = defaultdict(int)
        
        for i in range(len(s)):
            hm[s[i]] += 1
            hm[t[i]] -= 1

        for _, val in hm.items():
            if val != 0:
                return False
        return True