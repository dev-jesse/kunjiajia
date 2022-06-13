```python3
# Solution 1
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses
        queue = deque()
        res = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
            
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            res.append(curr)
            
            for nbr in graph[curr]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    queue.append(nbr)
                    
        return res if len(res) == numCourses else []
        
        
# Solution 2
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegrees = {}
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegrees[crs] = indegrees.get(crs, 0) + 1
        
        queue = collections.deque()
        for node in graph:
            if indegrees.get(node, 0) == 0:
                queue.append(node)
                
        res = []    
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nbr in graph[curr]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    queue.append(nbr)
                    
        return res if len(res) == numCourses else []
```
