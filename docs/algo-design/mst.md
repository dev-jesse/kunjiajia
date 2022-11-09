# Minimum Spanning Trees

A minimum spanning tree is used to find the best way to connect different nodes. It will be used when there are more than one possible route between two nodes which have different weights. The MST will be used to find out which route has the least weight. The MST problem can be solved using the Prim’s algorithm or Kruskal’s algorithm.
The Prim’s algorithm starts by connecting one vertex to another randomly chosen vertex. It then finds the cheapest edge that connects the two vertices and adds it to the tree. The process is repeated until all vertices are connected to one another with no edges left over.
Kruskal's algorithm starts by selecting two vertices from among all possible pairs of vertices and adding them to the MST as its first two nodes. Then for each unconnected pair of nodes, it finds the cheapest edge connecting them.

## Possible Properties
### Possible Property 1
**Property**

If e is a minimum-weight edge in connected graph G (where not all edge weights are necessarily distinct), then every minimum spanning tree of G contains e.

**Answer**

False! Imagine you have a graph G with all the same weights. Then some of the MSTs will now have e.

### Possible Property 2
**Property**

If e is a minimum-weight edge in connected graph G with distinct edge weights, then every
minimum spanning tree of G contains e.

**Answer**

True! Suppose that T is spanning tree that does not contain e. Let e be the edge that connects vertices a and b. T contains a path from a to b such that if T + {e} would create a cycle C. For all e' in C that is not e, we have that w(e') > w(e). For any e' we have T' = T + {e} - {e'} which results in w(T') < w(T), showing that T is not a MST. Proof by contradiction.

### Possible Property 3
**Property**

If G is a connected graph with distinct edge weights, and e is the maximum-weight edge
on some cycle C, then no minimum spanning tree of G contains e.

**Answer**

True! Suppose that we have e = (a, b), that is e connects vertices a and b. Then, since there exists
a cycle C, there must be another path from a to b such that an edge f has a lesser weight that e, that is 
w(f) < w(e). Therefore, let T' = T - e + f, well, w(T') < w(T) and hence T must not be a MST.

## Reverse-Delete
### Statement
Reverse-delete algorithm will always find a MST:
```
sort edges by non-increasing weight: w(e_1) >= ... >= w(e_m)
T <- E
for j <- 1,2,...,m:
    if T - {e_j} is connected:
        T <- T - {e_j}
return T
```

### Proof
Suppose that 