# Shortest Paths

This weeks tutorial was primary proof focused, with solutions that are not code based. Thus, I will dedicate this section to introduce the code for two shortest path finding algorithms.

## Djikstra's Algorithm

Dijkstra's algorithm is a single source path finding algorithm. That means, given a single source, we can find the shortest paths from this source node to every other (connected) node in the graph. The runtime of the program is O(|E|log|V|), since we explore every edge, and add newly discovered nodes from these edges into a min priority queue (insert/extract min in O(log n)).

**Code**

```python
from heapq import *

def dijkstra(graph, start, destination):
    # Start by initializing all nodes to infinite distance
    distance = {node: float('inf') for node in graph}
    distance[start] = 0  # Starting node distance to be 0

    heap = [(0, start)]
    # Unlike BFS, do not initialize visited set
    visited = set()

    while heap:
        dist, node = heappop(heap)
        # Add visited nodes here, not when checking neighbors
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor in visited: continue  # if checked neighbor then skip

            # 2 KEY NOTES
            #
            # 1. graph[node][neighbor] is the weight of the edge from 'node' to neighbor
            # 2. if condition checks that our current path is the shortest SO FAR
            if distance[node] + graph[node][neighbor] > distance[neighbor]:
                distance[neighbor] = distance[node] + graph[node][neighbor]
                heappush(heap, (distance[neighbor], neighbor))

    # Return the minimal distance to get from 'start' to 'destination'
    return d[destination]
```

## Floyd-Warshall Algorithm

The Floyd-Warshall algorithm differs from Dijkstra's algorithm in the way that it is not a single source algorithm. That is, we can obtain the shortest path between every pair of nodes in the graph (solves the all pairs problem).

**Code**

```python
def floyd_warshall(graph):
    n = len(graph)
    # Make a |V| x |V| matrix to keep track of all shortest pairs distance
    distance = [[float('inf)] * n for _ in range(n)]

    # Set the distance from a node to itself to be zero
    for i in range(n):
        distance[i][i] = 0

    # Get the shortest path by travelling via every vertex
    # (Note: see below videos for better understandings)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # See if travelling via node k is worth it
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Return the matrix to determine the all smallest pair paths
    return distance
```

## Resources

For anyone who is still stuck on the understanding, I will provide a few resources that helped me understand the concepts of shortest paths clearly.

**Djikstra**

1. [Dijkstra's algorithm in 3 minutes](https://www.youtube.com/watch?v=_lHSawdgXpI)

**Floyd-Warshall**

1. [Floyd–Warshall algorithm in 4 minutes](https://www.youtube.com/watch?v=4OQeCuLYj-4)
2. [G-42. Floyd Warshall Algorithm](https://www.youtube.com/watch?v=YbY8cVwWAvw)
