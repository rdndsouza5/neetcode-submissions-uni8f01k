class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res =[]
        self.backTrack([], nums, [False]* len(nums))
        return self.res

    def backTrack(self,perms:List[int], nums: List[int], pick:List[bool]):
        if len(perms) == len(nums):
            self.res.append(perms[:])
            return 
        for i in range(len(nums)):
            if not pick[i]:
                perms.append(nums[i])
                pick[i] = True
                self.backTrack(perms, nums, pick)
                perms.pop()
                pick[i]= False
                