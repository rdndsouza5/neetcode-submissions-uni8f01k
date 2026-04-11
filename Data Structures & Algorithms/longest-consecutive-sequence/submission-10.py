class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count,maxCount = 1,1
        
        l=1
        prev = nums[0]
        print(nums)
        while l<len(nums):
            if nums[l] == prev+1:
                print(count)
                count+=1
                maxCount= max(count, maxCount)
                prev = nums[l]
                l+=1
            elif nums[l]== nums[l-1]:
                l+=1
            else:
                count=1
                prev = nums[l]

                l+=1
            
        return maxCount