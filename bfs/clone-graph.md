```python3
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        nodes = self.get_nodes_bfs(node)
        clones = self.get_clone_map(nodes)
        self.attach_edges(nodes, clones)
        
        return clones[node]
        
    def get_nodes_bfs(self, node):
        queue = deque([node])
        visited = set([node])
        
        while queue:
            curr = queue.popleft()
            for nbr in curr.neighbors:
                if nbr not in visited:
                    queue.append(nbr)
                    visited.add(nbr)
        
        return list(visited)
    
    def get_clone_map(self, nodes):
        clones = {}
        for node in nodes:
            clones[node] = Node(node.val)
            
        return clones
    
    def attach_edges(self, nodes, clones):
        for node in nodes:
            new_node = clones[node]
            for nbr in node.neighbors:
                new_neighbor = clones[nbr]
                new_node.neighbors.append(new_neighbor)
        return
```
