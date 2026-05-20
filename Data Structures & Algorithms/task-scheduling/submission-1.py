class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:  
        cnt= Counter(tasks)

        maxHeap = [-i for i in cnt.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while q or maxHeap:
            time+=1
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and time== q[0][1]:
                val = q.popleft()
                heapq.heappush(maxHeap, val[0])


        return time