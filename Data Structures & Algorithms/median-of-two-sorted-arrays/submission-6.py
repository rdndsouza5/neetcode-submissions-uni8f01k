class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B= nums2, nums1
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B =  B, A
    
        l, r = 0, len(A)-1

        while True:
            i = (l+r)//2    

            j = half - i - 2 #because arrays are indexed by 0

            Aleft = A[i] if i >=0 else float("-infinity")
            Aright = A[i+1] if (i+1)< len(A) else float("infinity")

            Bleft = B[j] if j >=0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total %2:
                    return float(min(Aright, Bright))
                
                return (max(Aleft,Bleft)+ min(Bright,Aright))/float(2)

            elif Aleft> Bright:
                r=i-1
            else:
                l=i +1
                

