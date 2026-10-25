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

### Environment and methodology

- Language: Python 3.14.3
- Platform: Windows 11, build 26200
- Timer: `time.perf_counter()`
- Random generator: Python `random.Random`
- Graph seeds: 3538, 5538 and 8538 (base seed 2538 plus n)
- Warm-up: one execution of each algorithm on each graph, excluded from measurements
- Repetitions: three measurements per algorithm for each graph
- Timing boundary: algorithm execution only; graph generation is excluded
- Graphs are generated once and reused by both algorithms.

### Measurements

| Vertices (n) | Edges (m) | Kruskal runs (seconds) | Kruskal median (seconds) | Prim runs (seconds) | Prim median (seconds) |
|---:|---:|---|---:|---|---:|
| 1000 | 2999 | 0.004598, 0.005314, 0.005627 | 0.005314 | 0.006162, 0.005625, 0.005580 | 0.005625 |
| 3000 | 8999 | 0.016615, 0.017169, 0.016884 | 0.016884 | 0.026303, 0.021861, 0.027270 | 0.026303 |
| 6000 | 17999 | 0.058946, 0.056664, 0.044005 | 0.056664 | 0.077140, 0.072358, 0.054034 | 0.072358 |

### Correctness checks

For each graph, both algorithms returned the same minimum cost and component count. The selected forest contained n - components edges.

| n | Minimum cost | Components |
|---:|---:|---:|
| 1000 | 204458 | 1 |
| 3000 | 591462 | 1 |
| 6000 | 1193201 | 1 |

### Observations and limitations

Kruskal was faster than Prim in these three measurements. Both algorithms took longer on larger graphs. These results apply only to the tested graph generator, graph sizes and runtime environment. They do not establish that one algorithm is always faster.



## 9. Conclusion

The implementation uses iterative graph traversals where appropriate and supports disconnected graphs and important edge cases. Final verification includes public tests, custom tests, and benchmark measurements.