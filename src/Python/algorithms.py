
import heapq


def dsu(request):
    n = request["n"]
    parent = list(range(n))
    size = [1] * n
    components = n
    largest = 1 if n else 0
    states = []

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in request["operations"]:
        a, b = find(u), find(v)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            components -= 1
            largest = max(largest, size[a])
        states.append([components, largest])

    return {"states": states}


def kruskal(request):
    n = request["n"]
    edges = request["edges"]
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    cost = 0
    components = n
    edge_ids = []

    for edge_id, (u, v, w) in sorted(
        enumerate(edges), key=lambda item: (item[1][2], item[0])
    ):
        if u == v:
            continue
        a, b = find(u), find(v)
        if a == b:
            continue
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        components -= 1
        cost += w
        edge_ids.append(edge_id)

    return {"cost": cost, "edge_ids": edge_ids, "components": components}


def prim(request):
    n = request["n"]
    graph = [[] for _ in range(n)]

    for i, (u, v, w) in enumerate(request["edges"]):
        if u != v:
            graph[u].append((w, i, v))
            graph[v].append((w, i, u))

    visited = [False] * n
    edge_ids = []
    cost = 0
    components = 0

    for start in range(n):
        if visited[start]:
            continue
        components += 1
        visited[start] = True
        heap = [(w, i, start, v) for w, i, v in graph[start]]
        heapq.heapify(heap)

        while heap:
            w, edge_id, u, v = heapq.heappop(heap)
            if visited[v]:
                continue
            visited[v] = True
            cost += w
            edge_ids.append(edge_id)
            for nw, ni, to in graph[v]:
                if not visited[to]:
                    heapq.heappush(heap, (nw, ni, v, to))

    return {"cost": cost, "edge_ids": edge_ids, "components": components}


def _topological(n, graph):
    state = [0] * n
    order = []

    for start in range(n):
        if state[start]:
            continue
        state[start] = 1
        stack = [(start, 0)]

        while stack:
            u, i = stack[-1]
            if i == len(graph[u]):
                state[u] = 2
                order.append(u)
                stack.pop()
                continue

            v = graph[u][i]
            stack[-1] = (u, i + 1)

            if state[v] == 1:
                return None
            if state[v] == 0:
                state[v] = 1
                stack.append((v, 0))

    order.reverse()
    return order


def scc(request):
    n = request["n"]
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]

    for u, v in request["edges"]:
        graph[u].append(v)
        reverse[v].append(u)

    seen = [False] * n
    finish = []

    for start in range(n):
        if seen[start]:
            continue
        seen[start] = True
        stack = [(start, 0)]

        while stack:
            u, i = stack[-1]
            if i == len(graph[u]):
                finish.append(u)
                stack.pop()
                continue
            v = graph[u][i]
            stack[-1] = (u, i + 1)
            if not seen[v]:
                seen[v] = True
                stack.append((v, 0))

    component = [-1] * n
    count = 0

    for start in reversed(finish):
        if component[start] != -1:
            continue
        component[start] = count
        stack = [start]
        while stack:
            u = stack.pop()
            for v in reverse[u]:
                if component[v] == -1:
                    component[v] = count
                    stack.append(v)
        count += 1

    pairs = set()
    for u, v in request["edges"]:
        a, b = component[u], component[v]
        if a != b:
            pairs.add((a, b))

    return {
        "component": component,
        "condensation": [list(pair) for pair in sorted(pairs)]
    }


def topo(request):
    n = request["n"]
    graph = [[] for _ in range(n)]
    for u, v in request["edges"]:
        graph[u].append(v)

    order = _topological(n, graph)
    if order is None:
        return {"acyclic": False, "order": []}
    return {"acyclic": True, "order": order}


def dag(request):
    n = request["n"]
    source = request["source"]
    edges = request["edges"]
    graph = [[] for _ in range(n)]

    for edge_id, (u, v, w) in enumerate(edges):
        graph[u].append((v, w, edge_id))

    plain_graph = [[v for v, w, i in row] for row in graph]
    order = _topological(n, plain_graph)

    if order is None:
        return {"acyclic": False, "distance": [], "parent_edge": []}

    distance = [None] * n
    parent_edge = [-1] * n
    distance[source] = 0

    for u in order:
        if distance[u] is None:
            continue
        for v, w, edge_id in graph[u]:
            candidate = distance[u] + w
            if distance[v] is None or candidate < distance[v]:
                distance[v] = candidate
                parent_edge[v] = edge_id

    return {
        "acyclic": True,
        "distance": distance,
        "parent_edge": parent_edge
    }


def reconstruct_route(source, target, parent_edge, edges):
    if source == target:
        return [source]

    incoming = {}
    for edge_id, (u, v, *_) in enumerate(edges):
        incoming[edge_id] = (u, v)

    route = [target]
    current = target
    seen = set()

    while current != source:
        edge_id = parent_edge[current]
        if edge_id == -1 or edge_id in seen:
            return []
        seen.add(edge_id)
        u, v = incoming[edge_id]
        if v != current:
            return []
        current = u
        route.append(current)

    route.reverse()
    return route
