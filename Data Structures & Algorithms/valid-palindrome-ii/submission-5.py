class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r,c = 0, len(s)-1,True

        def isPallindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        while l<r:
            if s[l]!=s[r]:
                return isPallindrome(l+1,r) or isPallindrome(l,r-1)
            l+=1
            r-=1
                                
        return True
