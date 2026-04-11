class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        res = nums[-1]
        while l<= r:
            k= (l+r)//2
            res= min(res,nums[k] )

            if nums[r]<nums[k]:
                l= k+1
            else:
                r=k-1
        return res
