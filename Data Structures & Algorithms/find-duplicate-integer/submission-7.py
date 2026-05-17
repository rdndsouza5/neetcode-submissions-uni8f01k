class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1: r+1]
            i, j, k = l, 0, 0

            while j< len(left) and k< len(right):
                if left[j]< right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i]= right[k]
                    k+=1
                i+=1
            while j< len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            while k< len(right):
                arr[i] = right[k]
                k+=1
                i+=1
            return 


        def mergeSort(arr, l, r):
            if l>=r:
                return 
            m = (l+r)//2

            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)

            merge(arr, l, m, r)

            return arr

        mergeSort(nums, 0, len(nums))

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]