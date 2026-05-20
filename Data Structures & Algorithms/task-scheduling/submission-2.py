class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:  
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time= 0
        q= deque()

        while maxHeap or q:
            time +=1

            if not maxHeap:
                time = q[0][0]
            else:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt <0:
                    timeToWait = time+ n
                    q.append([timeToWait, cnt])
            if q and q[0][0] ==time:
                heapq.heappush(maxHeap, q.popleft()[1])
        return time