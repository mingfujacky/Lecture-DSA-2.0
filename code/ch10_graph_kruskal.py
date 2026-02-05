from ch10_graph_weighted import WeightedGraphList
from pathlib import Path


def minimum_cost_spanning_tree_kruskal(graph):
    # Step 1: Sort edges based on their weights
    edges = []
    for u in graph.L:
        for v, weight in graph.L[u]:
            edges.append((weight, u, v))
    edges.sort()  # Sort by weight

    # Step 2: Initialize a Disjoint Set (Union-Find) to keep track of connected components
    parent = list(range(graph.n))
    rank = [0] * graph.n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    # Step 3: Iterate through sorted edges and add them to the MST if they connect two different components
    mst_edges = []
    total_cost = 0
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            total_cost += weight

    return mst_edges, total_cost


g = WeightedGraphList()
file_path = Path.cwd() / "asset" / "txt" / "graph_mcst_kruskal.txt"
g.read_file(file_path)
mst, cost = minimum_cost_spanning_tree_kruskal(g)
print("Edges in the Minimum Cost Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} (weight: {weight})")
print(f"Total cost of the MST: {cost}")
