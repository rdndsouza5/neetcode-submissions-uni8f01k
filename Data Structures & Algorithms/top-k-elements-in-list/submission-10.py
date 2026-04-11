class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1+ count.get(i,0)
        
        res= []
        for i in range(k):
            curMax = 0
            curItem = 0
            for k,v in count.items():
                if v> curMax:
                    curItem = k
                    curMax = v
            res.append(curItem)
            del count[curItem]
        return res
