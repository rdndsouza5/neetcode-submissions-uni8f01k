class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i - 1]
        
        postFix = 1
        for i in range(len(nums)-2, -1 ,-1):
            postFix *= nums[i+1]
            res[i] = res[i] * postFix
        
 
        return res