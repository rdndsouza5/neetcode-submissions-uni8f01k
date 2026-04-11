class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        stack = []
        if not nums or k<1:
            return False
        for i in range(len(nums)):
            if len(stack) == k+1:
                stack.pop(0)
            if nums[i] in stack:
                return True
            stack.append(nums[i])
        return False