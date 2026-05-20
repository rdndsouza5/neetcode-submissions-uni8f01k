class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, total):
            if i==len(nums):
                return total
            including = dfs(i+1, total^nums[i])
            excluding = dfs(i+1, total)
            return including + excluding
        return dfs(0,0)