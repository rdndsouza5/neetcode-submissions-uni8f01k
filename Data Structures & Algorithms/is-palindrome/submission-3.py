class Solution:
    def isAlNum(self, c: str)-> bool:
        return ( ord('a')<=ord(c)<=ord('z') or
        ord('A')<=ord(c)<=ord('Z') or
        ord('0')<=ord(c)<= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l, r= 0, len(s)-1
        while l<r:
            if not self.isAlNum(s[l]):
                l+=1
                continue
            if not self.isAlNum(s[r]):
                r-=1
                continue
            if s[l].lower()!= s[r].lower():
                return False
            l+=1
            r-=1
        return True