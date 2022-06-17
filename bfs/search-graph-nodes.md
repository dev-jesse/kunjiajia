```python3
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        queue = collections.deque([node])
        visited = set([node])

        while queue:
            curr = queue.popleft()

            if values[curr] == target:
                return curr

            for nbr in curr.neighbors:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)

        return

```
