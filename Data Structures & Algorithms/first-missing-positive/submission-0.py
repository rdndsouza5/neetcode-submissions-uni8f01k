class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        while True:
            if i in nums:
                i+=1
            else:
                return i