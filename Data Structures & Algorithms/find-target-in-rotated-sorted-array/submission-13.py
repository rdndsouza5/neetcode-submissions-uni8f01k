class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2
            if  nums[m]> nums[r]:
                l=m+1
            else:
                r= m
        pivot = l

        def binary_search(left:int, right:int)-> int:
            while left <= right:
                mid = (left + right) //2
                if nums[mid]==target:
                    return mid
                if nums[mid]<target:
                    left= mid+1
                else:
                    right=mid-1
            return -1
        if target>= nums[pivot] and target<= nums[len(nums)-1]:
            return binary_search(pivot, len(nums)-1)
        else:
            return binary_search(0, pivot-1)

        

                    