class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *len(nums)
        
        preFix = 1
        for i in range(0, len(nums)):
            res[i]*= preFix
            preFix *= nums[i]
            print("pre",res[i])
        
        suFix = 1

        for i in range(len(nums)-1,-1, -1 ):
            res[i] *= suFix
            suFix *= nums[i]
        return res