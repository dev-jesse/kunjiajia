```python3
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    self.fill_bfs(grid, row, col, visited)
                    
        return islands
    
    def fill_bfs(self, grid, row, col, visited):
        queue = deque([(row, col)])
        visited.add((row, col))
        
        while queue:
            r, c = queue.popleft()
            
            for dx, dy in DIRECTIONS:
                next_r = r + dx
                next_c = c + dy
                
                if next_r in range(len(grid)) and \
                next_c in range(len(grid[0])) and \
                (next_r, next_c) not in visited and \
                grid[next_r][next_c] == "1":
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
```
