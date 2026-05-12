class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = 0
        while idx< len(nums):
            if nums[idx]> 0 and nums[idx]<= len(nums): 
                i = nums[idx]-1
                if nums[idx] == nums[i]:
                    idx +=1
                    continue 
                nums[idx], nums[i]= nums[i], nums[idx]
            else:
                idx +=1
                
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1