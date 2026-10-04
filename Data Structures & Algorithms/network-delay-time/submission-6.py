class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v,w))
        
        minH = [(0, k)]
        visited = set()
        res = 0

        while minH:
            w1, n1 = heapq.heappop(minH)

            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res, w1)

            for n2, w2 in edges[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minH, (w1+w2, n2))



        return -1 if len(visited) != n else res