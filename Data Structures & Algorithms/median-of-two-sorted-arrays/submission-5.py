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
        
        if (len(nums1)+len(nums2))%2 ==0:
            right = 0
            if l1> r1:
                right = nums2[l2]
            elif l2>r2:
                right = nums1[l1]
            else:
                right = min(nums1[l1],nums2[l2])
            left =0
            if l1-1<0:
                left = nums2[l2-1]
            elif l2-1<0:
                left = nums1[l1-1]
            else:
                left = max(nums1[l1-1],nums2[l2-1])
            print(right,left)
            return float(right+left)/float(2)
        print("herer")
        if l1> r1:
            return float(nums2[l2])
        elif l2>r2:
            return float(nums1[l1])
        return float(min(nums1[l1],nums2[l2]))
            


