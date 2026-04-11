class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return [hashMap[nums[i]],i]
            hashMap[target-nums[i]]=i
        return [0,0]

        