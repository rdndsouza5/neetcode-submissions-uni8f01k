class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        arr = [(0, k)]

        seen = set()
        t = 0
        while arr:
            w1, n1 = heapq.heappop(arr)
            if n1 in seen:
                continue
            t = max(t, w1)
            seen.add(n1)

            for n2, w2 in edges[n1]:
                if n2 in seen:
                    continue
                heapq.heappush(arr, ( w1+w2, n2))

        return t if len(seen)== n else -1