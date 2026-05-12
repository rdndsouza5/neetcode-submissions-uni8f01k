class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength =  0
        for i in nums:
            if (i-1) in numSet:
                continue
            
            curLength = 0
            curr = i
            while curr in numSet:
                curr += 1
                curLength +=1
            maxLength = max(curLength, maxLength)
        return maxLength


