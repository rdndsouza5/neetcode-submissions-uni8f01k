import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partion(arr, low, high):
            pivot_idx = (low+high)//2
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

            pivot = arr[high]
            i = low-1

            for j in range(low, high):
                if arr[j]<= pivot:
                    i+=1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def quickSort(arr, low, high):
            if low< high:
                p= partion(arr, low, high)
                quickSort(arr,low, p-1)
                quickSort(arr,p+1, high)
        quickSort(nums,0, len(nums)-1)
        return nums