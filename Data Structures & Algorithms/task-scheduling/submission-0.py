class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        hm = {}
        for i in tasks:
            hm[i] = -1 + hm.get(i, 0)

        maxHeap = [i for i in hm.values()]

        heapq.heapify(maxHeap)
        

        time = 0
        q= deque()

        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] ==time:
                v= q.popleft()
                heapq.heappush(maxHeap,v[0])

        return time