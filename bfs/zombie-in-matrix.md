```python3
from typing import (
    List,
)

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid: List[List[int]]) -> int:
        # Collect initial zombies
        queue = collections.deque()
        distance = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    distance[(i, j)] = 0

        # Infect neighbor humans
        while queue:
            i, j = queue.popleft()
            for dx, dy in DIRECTIONS:
                x, y = i + dx, j + dy
                if self.is_valid(grid, distance, x, y):
                    distance[(x, y)] = distance[(i, j)] + 1
                    queue.append((x, y))
                    # If you want to visualize you can do grid[x][y] = 1
                    # but otherwise it is covered in the distance case.

        # Check for surviving humans
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) not in distance:
                    return -1

        return max(distance.values())


    def is_valid(self, grid, distance, x, y):
        if not 0 <= x < len(grid):
            return False
        if not 0 <= y < len(grid[0]):
            return False
        if (x, y) in distance:
            return False

        return not grid[x][y]
```
