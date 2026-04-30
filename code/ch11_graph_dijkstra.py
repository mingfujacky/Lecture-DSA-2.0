from ch08_heap import Heap
from ch11_graph_weighted import WeightedGraphList
from pathlib import Path
import math


def dijkstra(g, start_node):
    """
    Computes the shortest path from start_node to all other nodes.
    Returns:
        distances: A dictionary mapping nodes to their min distance.
        predecessors: A dictionary to reconstruct the shortest paths.
    """
    # 1. Initialization
    # Set all distances to infinity ($ \infty $) and the start node to 0
    distances = {node: math.inf for node in range(g.n)}
    distances[start_node] = 0
    predecessors = {node: None for node in range(g.n)}

    # 2. Priority Queue (min-heap) to explore the closest nodes first
    # Format: (current_distance, node_index)
    # Use Heap with negated distance so smaller distances have higher priority
    pq = Heap(element_priority=lambda x: -x[0])
    pq.insert((0, start_node))

    while not pq.is_empty():
        current_distance, u = pq.top()

        # Skip if we already found a shorter path to u
        if current_distance > distances[u]:
            continue

        # 3. Relaxation Step
        # Look at all neighbors 'v' of the current node 'u'
        for v, weight in g.L[u]:
            distance = current_distance + weight

            # If this new path to 'v' is shorter, update it
            if distance < distances[v]:
                distances[v] = distance
                predecessors[v] = u
                pq.insert((distance, v))

    return distances, predecessors


def get_path(predecessors, target):
    """Helper function to trace the path back from target to source."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    return path[::-1]  # Reverse the list to get Start -> Target


if __name__ == "__main__":
    g = WeightedGraphList()
    file_path = Path.cwd() / "asset" / "txt" / "graph_shortest_path_dijkstra.txt"
    g.read_file(file_path)
    print("--- Graph Adjacency List ---")
    g.print()

    # Calculate Shortest Paths from Node 0
    start_node = 0
    dists, preds = dijkstra(g, start_node)
    print(f"--- Dijkstra Results (Source: {start_node}) ---")
    for node in range(g.n):
        path = get_path(preds, node)
        dist = dists[node]
        print(f"To Node {node}: Distance = {dist:2}, Path = {path}")
