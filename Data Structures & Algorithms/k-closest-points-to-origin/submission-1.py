class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            val = (x**2 + y**2)
            heapq.heappush(maxHeap, [val, x,y ])
          
        res = []
        while k>0:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
            k-=1
        return res