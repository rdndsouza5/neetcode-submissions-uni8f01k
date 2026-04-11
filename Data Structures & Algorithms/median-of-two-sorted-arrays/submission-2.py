class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2, r1, r2 = 0, 0, len(nums1)-1, len(nums2)-1

        while l1+l2 < ((len(nums1)+ len(nums2))//2):
            if l1>r1:
                l2 +=1
            elif l2>r2:
                l1 += 1
            elif nums1[l1]<nums2[l2]:
                l1+=1
            else:
                l2+=1
        mid = 0
        if (len(nums1)+ len(nums2))%2 == 0:
            right_val = 0
            if l1 > r1: right_val = nums2[l2]
            elif l2 > r2: right_val = nums1[l1]
            else: right_val = min(nums1[l1], nums2[l2])
            
            left_val = 0
            if l1 - 1 < 0: left_val = nums2[l2-1]
            elif l2 - 1 < 0: left_val = nums1[l1-1]
            else: left_val = max(nums1[l1-1], nums2[l2-1])
            
            mid = (float(left_val) + float(right_val)) / 2.0
        else:
            if l1>r1:
                mid = float(nums2[l2])
            elif l2>r2:
                mid = float(nums1[l1])
            else: 
                mid = float(min(nums1[l1], nums2[l2]))
        return mid