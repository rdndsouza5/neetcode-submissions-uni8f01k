class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hm:
                return [hm[rem], i]
            hm[nums[i]] = i











