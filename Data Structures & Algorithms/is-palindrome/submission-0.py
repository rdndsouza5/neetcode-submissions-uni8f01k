class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r=0,len(s)-1
        while(l<r):
            while (l<r) and not self.alNum(s[l]):
                l=l+1
            while (l<r) and not self.alNum(s[r]):
                r=r-1
            print(s[l].lower)
            if s[l].lower() != s[r].lower():
                return False
            print(s[l],"=",s[r])
            l,r=l+1,r-1
        return True

        
    

    def alNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))