class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res= [0] *n

        prefix, suffix = 1, 1

        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        for i in range(n-1, -1, -1):
            res[i]*= suffix
            suffix = suffix *nums[i]
      
        return res