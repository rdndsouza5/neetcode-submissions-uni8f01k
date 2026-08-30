class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hm = {}
        res = 0
        seq = [1] *len(nums)
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    seq[i] = max(seq[i], seq[j]+1)
            
            res = max(res, seq[i])
        return res

