class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        mp = {}
        for i in nums:
            mp[i] = 1+ mp.get(i, 0)

        index = 0
        for i in range(3):
            while mp.get(i,0):
                mp[i]-=1
                nums[index]= i
                index+=1