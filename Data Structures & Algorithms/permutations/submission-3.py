class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False]*len(nums))
        return self.res


    def backtrack(self, perms: List[int], nums: List[int], picks:List[bool]):
        if len(perms)==len(nums):
            self.res.append(perms.copy())
            return
        for i in range(len(nums)):
            if not picks[i]:
                perms.append(nums[i])
                picks[i]=True
                self.backtrack(perms, nums, picks)
                perms.pop()
                picks[i]=False
            
                
