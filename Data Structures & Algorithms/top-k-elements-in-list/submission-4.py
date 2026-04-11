class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]= count.get(i,0)+1
        

        res =[]
        for i in range(k):
            mk,mv=0,0
            for k,v in count.items():
                if v>mv:
                    mv=v
                    mk=k
            res.append(mk)
            del count[mk]
        return res
                
