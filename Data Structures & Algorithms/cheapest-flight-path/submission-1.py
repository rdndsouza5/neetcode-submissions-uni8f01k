class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s, d, c in flights:
            adj[s].append((d, c))

        
        minH = [(0, src, 0)]
        visited = set()

        while minH:
            cost, pos, stops = heapq.heappop(minH)
            if pos == dst:
                return cost
            if (pos, stops) in visited or stops >k:
                continue


            for sDst, sDstCost in adj[pos]:
                if sDst in visited:
                    continue
                heapq.heappush(minH, (cost+sDstCost, sDst, stops+1))

            visited.add((pos, stops))
        
        return -1