class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0]*n

        for follower, leader in trust:
            count[leader -1] +=1
            count[follower -1] -=1
            
        for i in range(len(count)):
            if count[i]==n-1:
                return i+1
        return -1