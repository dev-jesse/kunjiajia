```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        nodes = self.get_nodes(head)
        clones = self.clone_nodes(nodes)
        self.attach_clones(nodes, clones)
        
        return clones[head]
    
    def get_nodes(self, node):
        result = []
        while node is not None:
            result.append(node)
            node = node.next
            
        return result
            
    def clone_nodes(self, nodes):
        clones = {}
        for node in nodes:
            clones[node] = Node(node.val, node.next)
        return clones
    
    def attach_clones(self, nodes, clones):
        for node in nodes:
            if node.next:
                clones[node].next = clones[node.next]
            if node.random:
                clones[node].random = clones[node.random]
```
