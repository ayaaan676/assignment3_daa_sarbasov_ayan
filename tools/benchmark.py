
import platform
import random
import statistics
import time
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src" / "Python"))

from algorithms import kruskal, prim


def make_graph(n, seed):
    rng = random.Random(seed)
    edges = []

    # Ensure the graph is connected.
    for v in range(1, n):
        u = rng.randrange(v)
        w = rng.randint(1, 1000)
        edges.append([u, v, w])

    # Add extra edges.
    extra = 2 * n
    for _ in range(extra):
        u = rng.randrange(n)
        v = rng.randrange(n)
        w = rng.randint(1, 1000)
        edges.append([u, v, w])

    return edges


def measure(function, request):
    start = time.perf_counter()
    result = function(request)
    elapsed = time.perf_counter() - start
    return result, elapsed


def main():
    print("Python:", platform.python_version())
    print("Platform:", platform.platform())
    print("Timer: time.perf_counter")
    print("Warm-up: one run per algorithm, excluded from measurements")
    print("Timing includes algorithm execution, excludes graph generation")
    print("Seed: 2538")
    print()

    for n in [1000, 3000, 6000]:
        edges = make_graph(n, 2538 + n)
        request = {"n": n, "edges": edges}

        # Warm-up on the same graph.
        kruskal(request)
        prim(request)

        k_times = []
        p_times = []
        k_result = None
        p_result = None

        for _ in range(3):
            k_result, elapsed = measure(kruskal, request)
            k_times.append(elapsed)

            p_result, elapsed = measure(prim, request)
            p_times.append(elapsed)

        assert k_result["cost"] == p_result["cost"], (
            "Kruskal and Prim returned different costs"
        )
        assert k_result["components"] == p_result["components"]
        assert len(k_result["edge_ids"]) == n - k_result["components"]
        assert len(p_result["edge_ids"]) == n - p_result["components"]

        print(f"Graph: n={n}, m={len(edges)}")
        print("Kruskal timings (seconds):", [round(x, 6) for x in k_times])
        print("Kruskal median:", round(statistics.median(k_times), 6))
        print("Prim timings (seconds):", [round(x, 6) for x in p_times])
        print("Prim median:", round(statistics.median(p_times), 6))
        print("Minimum cost:", k_result["cost"])
        print("Components:", k_result["components"])
        print()


if __name__ == "__main__":
    main()