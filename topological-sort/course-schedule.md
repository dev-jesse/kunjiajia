```python3
from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(num_courses)}
        indegrees = {i: 0 for i in range(num_courses)}
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegrees[crs] += 1

        queue = collections.deque([crs for crs, val in indegrees.items() if not val])
        result = []
        while queue:
            crs = queue.popleft()
            result.append(crs)
            for nbr in graph[crs]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    queue.append(nbr)
        
        return len(result) == num_courses
```
