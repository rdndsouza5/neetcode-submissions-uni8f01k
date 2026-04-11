class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod , cnt = 1, 0
        n = len(nums)

        for i in nums:
            if i:
                prod *= i
            else:
                cnt += 1 
        if cnt > 1: return [0] * n

        res = [0] * n
        for i, c in enumerate(nums):
            if cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod//c
        return res