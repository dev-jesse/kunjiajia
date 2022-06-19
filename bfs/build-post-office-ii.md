```python3
class Grid:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortest_distance(self, grid):
        if not grid:
            return -1

        # Every time we reach a house outwardly expand distance
        dp_houses = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp_distance = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        num_of_houses = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == Grid.HOUSE:
                    self.bfs(grid, i, j, dp_houses, dp_distance)
                    num_of_houses += 1

        # Iterate the houses and distances at each part, and check if suitable
        # to replace the min_distance
        min_distance = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dp_houses[i][j] == num_of_houses and dp_distance[i][j] < min_distance:
                    min_distance = dp_distance[i][j]

        return min_distance if min_distance != float('inf') else -1
    
    def bfs(self, grid, i, j, dp_houses, dp_distance):
        queue = collections.deque([(i, j)])
        visited = set([(i, j)])
        distance = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if dp_distance[i][j] == float('inf'):
                    dp_distance[i][j] = 0
                dp_distance[i][j] += distance
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if not self.is_valid(grid, x, y, visited):
                        continue
                    visited.add((x, y))
                    dp_houses[x][y] += 1
                    if grid[x][y] == Grid.EMPTY:
                        queue.append((x, y))
            distance += 1

    def is_valid(self, grid, i, j, visited):
        if not 0 <= i < len(grid):
            return False
        if not 0 <= j < len(grid[0]):
            return False
        if (i, j) in visited:
            return False
        return grid[i][j] != Grid.WALL
```
