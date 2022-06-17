```python3
# Version 1
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
                
# Version 2 (Shortened)
from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return
        
        visited = {node: UndirectedGraphNode(node.label)}
        queue = collections.deque([node])

        while queue:
            curr = queue.popleft()
            for nbr in curr.neighbors:
                if nbr not in visited:
                    visited[nbr] = UndirectedGraphNode(nbr.label)
                    queue.append(nbr)
                visited[curr].neighbors.append(visited[nbr])

        return visited[node]
```
