class Solution:
    def recursion_search(self, nums: List[int], l: int, r:int, target: int):
        if l>r:
            return -1
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m]>target:
            return self.recursion_search(nums, l, m-1, target)
        else:
            return self.recursion_search(nums, m+1, r, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.recursion_search(nums, 0, len(nums)-1, target)


    