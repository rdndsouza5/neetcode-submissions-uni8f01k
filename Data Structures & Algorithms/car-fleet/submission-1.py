class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        
        pair.sort(reverse=True)
        stack = []
        curMin = (target- pair[0][0])/pair[0][1]
        total = 1
        for p, s in pair:
            curTime = (target- p)/s
            print(curTime)
            if curTime> curMin:
                total+=1
                curMin = curTime
        return total

