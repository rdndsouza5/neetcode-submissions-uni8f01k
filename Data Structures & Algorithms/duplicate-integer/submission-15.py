class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {n for n in nums}
        return len(a)!= len(nums)