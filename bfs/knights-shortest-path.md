```python3
from collections import deque
from typing import List
from lintcode import Point

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]

            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy

                if self.is_valid(next_x, next_y, grid, distance):
                    queue.append((next_x, next_y))
                    distance[(next_x, next_y)] = distance[(x, y)] + 1

        return -1

    def is_valid(self, x, y, grid, distance):
        if x not in range(len(grid)):
            return False

        if y not in range(len(grid[0])):
            return False

        if (x, y) in distance:
            return False

        return not grid[x]
```
