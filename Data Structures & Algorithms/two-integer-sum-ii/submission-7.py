class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            res= target- numbers[i]
            l=i+1
            r= len(numbers)-1
            while l<=r:
                m= (r+l)//2 
                if numbers[m]>res:
                    r= m-1
                elif numbers[m]<res:
                    l= m+1
                else:
                    return [i+1, m+1]