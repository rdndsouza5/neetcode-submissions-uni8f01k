class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for n in nums:
            if n in check:
                return n
            check.add(n)