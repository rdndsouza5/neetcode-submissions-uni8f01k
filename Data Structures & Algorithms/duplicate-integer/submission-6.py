class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset=set()
        for i in nums:
            hset.add(i)
        return len(hset)!=len(nums)