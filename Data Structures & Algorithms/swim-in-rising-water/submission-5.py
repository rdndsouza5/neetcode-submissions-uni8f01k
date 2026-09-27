class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        minH = [(0, 0, 0)]
        t = 0

        r, c = 0, 0

        directions = [(0, 1), (1, 0), (-1, 0),(0, -1)]

        t = grid[r][c]

        if 1==ROWS and 1==COLS:
            return 0
        while True:
            while minH[0][0] <= t:
                _, r, c  = heapq.heappop(minH)
                if (r, c) in visited:
                    continue

                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in visited or (nr < 0 or nr >= ROWS or nc<0 or nc >= COLS):
                        continue
                    if nr == ROWS -1 and nc == COLS -1:
                        return max(t, grid[nr][nc])
                    
                    heapq.heappush(minH, (grid[nr][nc], nr, nc))
            t+=1