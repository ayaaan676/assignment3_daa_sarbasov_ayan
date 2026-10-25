# Analysis — Assignment 3: Graph Algorithms

## 1. Disjoint Set Union (DSU)

The DSU algorithm maintains connected components using path compression and union by size. These optimizations make operations very fast in practice.

**Time complexity:** Nearly O(1) amortized per operation.

## 2. Kruskal's Algorithm

Kruskal's algorithm sorts edges by weight and adds an edge if it connects two different components. DSU is used to detect cycles.

**Time complexity:** O(m log m), where m is the number of edges.

## 3. Prim's Algorithm

Prim's algorithm builds a minimum spanning forest by repeatedly selecting the smallest available edge using a priority queue.

**Time complexity:** O((n + m) log m), where n is the number of vertices and m is the number of edges.

## 4. Strongly Connected Components (SCC)

Kosaraju's algorithm uses two graph traversals. The first traversal calculates finishing order, and the second traversal on the reversed graph identifies components.

**Time complexity:** O(n + m).

## 5. Topological Sorting

The algorithm uses three states: unvisited, visiting, and visited. A back edge to a visiting vertex indicates a cycle. An iterative DFS avoids recursion-depth problems.

**Time complexity:** O(n + m).

## 6. Shortest Paths in a DAG

The algorithm first checks whether the graph is acyclic. It then processes vertices in topological order and relaxes outgoing edges. Negative edge weights are supported in a DAG.

**Time complexity:** O(n + m).

## 7. Testing and Edge Cases

The implementation was checked using the provided public tests. Additional testing should cover empty graphs, isolated vertices, self-loops, parallel edges, disconnected graphs, negative edge weights, and directed cycles.

## 8. Benchmark Results

Benchmark measurements comparing Kruskal's and Prim's algorithms must be recorded after running both algorithms on the same graphs at three different sizes. At least three timings per algorithm should be collected for each size, and the median should be reported.

## 9. Conclusion

The implementation uses iterative graph traversals where appropriate and supports disconnected graphs and important edge cases. Final verification includes public tests, custom tests, and benchmark measurements.