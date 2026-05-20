class Solution:
    def combinationSum2(self, candidates, target):
        self.count = Counter(candidates)
        nums = [i for i in self.count.keys()]
        self.res = []
        self.backTrack(nums, target, [], 0)
        return  self.res

    def backTrack(self, nums, target, cur, i):
        if target == 0:
            self.res.append(cur.copy())
            return 
        
        if target< 0 or i>= len(nums):
            return 
        if self.count[nums[i]]>0:
            cur.append(nums[i])
            self.count[nums[i]]-=1
            self.backTrack(nums, target-nums[i], cur, i)
            self.count[nums[i]]+=1

            cur.pop()
        self.backTrack(nums, target, cur, i+1)