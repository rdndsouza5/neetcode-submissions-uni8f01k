class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = []

        for i,n in enumerate(nums):
            tmp.append([n,i])

        tmp.sort()

        i, j = 0, len(nums)-1

        while i < j:
            curr = tmp[i][0] + tmp[j][0]
            if curr == target:
                return [min(tmp[i][1], tmp[j][1]), max(tmp[i][1], tmp[j][1])]
            elif curr < target:
                i+=1
            else:
                j-=1