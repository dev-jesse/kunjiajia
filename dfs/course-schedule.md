```python3
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = set()
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True
            
            visited.add(node)
            for nbr in graph[node]:
                if not dfs(nbr): return False
                    
            graph[node] = []
            visited.remove(node)
            
            return True
        
        for node in range(numCourses):
            if not dfs(node): return False
            
        return True
```
