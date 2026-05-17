class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            val = -(x**2 + y**2)
            heapq.heappush(maxHeap, [val, x,y ])
            if len(maxHeap)> k:
                heapq.heappop(maxHeap)
            
        res = []
        while maxHeap:
            val = heapq.heappop(maxHeap)
            res.append([val[1],val[2]])
        return res