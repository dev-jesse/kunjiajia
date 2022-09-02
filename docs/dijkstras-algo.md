# Dijkstra's Algorithm
## Explanation
<iframe width="100%" height="400vh" src="https://www.youtube.com/embed/_UaBUG5D1MA" title="Dijkstra's Algorithm | Explanation & Example" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Template Code
```py
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
