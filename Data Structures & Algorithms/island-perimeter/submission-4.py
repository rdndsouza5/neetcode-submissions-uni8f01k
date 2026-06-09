class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        paths = [[1, 0],[-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))

            seen.add((r,c))

            perimeter = 0

            while queue:
                r, c = queue.popleft()
                for x, y in paths:
                    rx, cy = r+x, c+y
                    if rx<0 or rx>=len(grid) or cy<0 or cy>=len(grid[0]) or grid[rx][cy] ==0:
                        perimeter +=1
                    elif (rx, cy) not in seen:
                        seen.add((rx, cy))
                        queue.append((rx, cy))
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return bfs(r,c)
