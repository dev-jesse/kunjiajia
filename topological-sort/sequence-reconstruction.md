```python3
from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # Check that org and seqs have same nodes (if not cannot recreate)
        all_nodes = set().union(*[set(seq) for seq in seqs])
        if len(all_nodes) != len(org):
            return False

        # Create a graph
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
                indegrees[seq[i + 1]] += 1

        # Topological sort and check for uniqueness (queue len == 1)
        queue = collections.deque([node for node in org if indegrees.get(node, 0) == 0])
        result = []
        while len(queue) == 1:
            # Can also break if len(queue) > 1
            node = queue.popleft()
            result.append(node)
            for nbr in graph[node]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    queue.append(nbr)

        return result == org

```
