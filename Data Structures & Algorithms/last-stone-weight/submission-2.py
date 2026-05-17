class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones)==1:
            return stones[0]
        arr = [-s for s in stones]
        heapq.heapify(arr)

        while len(arr)>1:
            left = heapq.heappop(arr)
            right = heapq.heappop(arr)
            if left == right:
                continue
            res = left + (-right)
            heapq.heappush(arr,res)
            
        if len(arr)==1:
            return -heapq.heappop(arr)
        return 0