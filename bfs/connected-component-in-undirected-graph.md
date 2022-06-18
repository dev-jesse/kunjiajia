```python3
from typing import (
    List,
)
from lintcode import (
    UndirectedGraphNode,
)

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        visited = set()
        result = []
        for node in nodes:
            if node not in visited:
                result.append(self.get_connected(visited, node))

        return result

    def get_connected(self, visited, start):
        visited.add(start)
        queue = collections.deque([start])
        connected_component = []

        while queue:
            node = queue.popleft()
            connected_component.append(node.label)
            for nbr in node.neighbors:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)

        return sorted(connected_component)
```
