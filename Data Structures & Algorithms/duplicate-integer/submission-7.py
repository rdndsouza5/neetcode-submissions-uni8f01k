class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset=set()
        for i in nums:
            if i not in hset:
                hset.add(i)
            else:
                return True
        return False