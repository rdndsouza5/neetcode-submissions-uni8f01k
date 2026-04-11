class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count =defaultdict(int)

        minVal, maxVal = 0,0
        for val in nums:
            count[val]+=1
            if val < minVal:
                minVal= val
            elif val > maxVal:
                maxVal= val
            
        index =0
        print(count,minVal,maxVal)
        for val in range(minVal, maxVal+1):
            while count[val]>0:
                nums[index]=val
                count[val]-=1
                index+=1
            
        return nums