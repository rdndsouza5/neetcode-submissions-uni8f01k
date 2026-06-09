class Solution:
    def check(self, nums: List[int]) -> bool:
        oneNonSorted = False

        for i in range(1, len(nums)):
            if nums[i-1]>nums[i]:
                if oneNonSorted:
                    return False
                oneNonSorted = True
        if oneNonSorted:
            if nums[-1]> nums[0]:
                return False
        return True