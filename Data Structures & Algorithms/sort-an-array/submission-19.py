class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
    def partition(self, nums,l , r)->int:
        m = (l+r)>>1
        nums[l+1], nums[m] = nums[m], nums[l+1]

        if nums[l]> nums[r]:
            nums[r], nums[l] = nums[l], nums[r]
        if nums[l] > nums[l+1]:
            nums[l+1], nums[l] = nums[l], nums[l+1]
        if nums[l+1] > nums[r]:
            nums[r], nums[l+1] = nums[l+1], nums[r]
        

        pivot = nums[l+1]
        i= l+1
        j = r


        while True:
            while True:
                i+=1
                if nums[i] >= pivot:
                    break
            while True:
                j-=1
                if nums[j]<= pivot:
                    break
            if i>j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            
        nums[j], nums[l+1] = nums[l+1], nums[j]
        return j
            

    def quickSort(self, nums, l, r):
        if l+1 >= r:
            if l+1 ==r  and nums[l] > nums[r]:
                nums[r], nums[l] = nums[l], nums[r]
            return 
        j = self.partition(nums, l, r)
        self.quickSort(nums, l, j-1)
        self.quickSort(nums, j+1, r)
    