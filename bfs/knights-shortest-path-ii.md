```python3
from typing import (
    List,
)

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        queue = collections.deque([(0, 0)])
        distance = {(0, 0): 0}
        final = (len(grid) - 1, len(grid[0]) - 1)

        while queue:
            x, y = queue.popleft()

            if (x, y) == final:
                return distance[final]

            for next_x, next_y in ((x + 1, y + 2), (x - 1, y + 2), 
            (x + 2, y + 1), (x - 2, y + 1)):
                if not self.is_valid(grid, distance, next_x, next_y):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))

        return -1

    def is_valid(self, grid, visited, x, y):
        if not 0 <= x < len(grid):
            return False
        if not 0 <= y < len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        
        return not grid[x][y]
```
