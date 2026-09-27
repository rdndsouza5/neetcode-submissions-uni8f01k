class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = [(0, 0, 0)]
        
        rows, cols = len(heights)-1, len(heights[0])-1

        visit = set()

        directions = [(1, 0), (0,1),(0, -1), (-1, 0)]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r, c))

            if r == rows and c == cols:
                return diff
            h = heights[r][c]
            for dx, dy in directions:
                dr, dc = r+dx, c+dy
                if dr<0 or dr> rows or dc<0 or dc>cols or (dr, dc) in visit:
                    continue
                dh = heights[dr][dc]

                heapq.heappush(minHeap, (max(diff , abs(h-dh)), dr, dc))
        return 0