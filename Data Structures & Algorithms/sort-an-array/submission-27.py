class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    def partition(self,nums, l, r):
        mid = (l+r)>>1
        nums[l+1], nums[mid] = nums[mid], nums[l+1]

        if nums[l]>nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        if nums[l]>nums[l+1]:
            nums[l], nums[l+1] = nums[l+1], nums[l]
        if nums[l+1] > nums[r]:
            nums[l+1], nums[r] = nums[r], nums[l+1]
        
        pivot = nums[l+1]
        i = l+1
        j= r

        while True:
            while True:
                i+=1
                if not nums[i]< pivot:
                    break
            while True:
                j-=1
                if not nums[j]> pivot:
                    break
            if i> j:
                break
            nums[i], nums[j] = nums[j],  nums[i]
        
        nums[j], nums[l+1] = nums[l+1],  nums[j]

        return j
            


    def quickSort(self,nums, l, r):
        if l+1>=r :
            if r == l+1 and nums[r]< nums[l]:
                nums[r], nums[l]=nums[l], nums[r]
            return 
            
        p = self.partition(nums,l, r)
        self.quickSort(nums,l, p)
        self.quickSort(nums, p, r)
