class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)-1
        
        while l<=h:
            m=int((h+l)/2)
            print(m)
            if nums[m]>target:
                h=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m

        return -1
