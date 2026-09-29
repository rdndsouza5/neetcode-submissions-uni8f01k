class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0:
            return False
        target = total//2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                s = t+ nums[i]
                if s == target:
                    return True
                nextDp.add(t)
                nextDp.add(s)
            dp = nextDp
        return False