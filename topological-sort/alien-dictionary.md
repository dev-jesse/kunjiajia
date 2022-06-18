```python3
from typing import (
    List,
)
from heapq import *

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Create graph
        graph = {ch: [] for word in words for ch in word}
        indegrees = {ch: 0 for word in words for ch in word}
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    indegrees[words[i + 1][j]] += 1
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1 and \
                len(words[i]) > len(words[i + 1]):
                    return ''

        # Topological sort w/ heap to keep lexicographical order
        heap = [ch for ch in indegrees if indegrees[ch] == 0]
        heapify(heap)
        result = []

        while heap:
            ch = heappop(heap)
            result.append(ch)
            for next_ch in graph[ch]:
                indegrees[next_ch] -= 1
                if indegrees[next_ch] == 0:
                    heappush(heap, next_ch)

        # Check that all nodes are popped from graph (all nodes used)
        return ''.join(result) if len(result) == len(graph) else ''
```
