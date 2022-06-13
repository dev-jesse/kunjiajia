```python3
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegrees = {}

        for node in graph:
            for nbr in node.neighbors:
                indegrees[nbr] = indegrees.get(nbr, 0) + 1

        queue = collections.deque()
        for node in graph:
            if indegrees.get(node, 0) == 0:
                queue.append(node)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nbr in curr.neighbors:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    queue.append(nbr)

        return res
```
