class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        memo = {}
        def dfs(i, target):
            if target == 0:
                return True
            if target <0 or i>=len(nums):
                return False
            key = (i, target)
            if key in memo:
                return memo[key]
            
            res=  dfs(i+1, target- nums[i]) or dfs(i+1, target)
            memo[key] = res
            return res
        return dfs(0, sum(nums)/2)