class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows , cols = len(grid), len(grid[0])
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def bfs(r, c):
            queue = deque([(r,c)])
            visited.add((r, c ))
            perimeter = 0

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>= rows or ny>=cols or grid[nx][ny]==0:
                        perimeter +=1
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return bfs(i, j)