class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n not in a:
            a.add(n)
            temp=0
            while(n!=0):
                b=n%10
                temp= temp+ b**2
                n=n//10
                print(n)
            n=temp
            if n==1:
                return True
        return False
        