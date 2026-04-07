from ch10_graph import Graph
from ch07_queue_list import Queue
from pathlib import Path


def bfs_traverse(graph, key):
    """Perform a breadth-first traversal from a given vertex."""
    if isinstance(key, str) and key.isdigit():
        key = int(key)
    if not graph.has_vertex(key):
        raise ValueError(f"Start vertex {key} does not exist!")

    print(f"Starting BFS traversal from vertex: {key}")
    visited = {v: False for v in graph._adj}
    queue = Queue()
    traversal_order = []

    queue.enqueue(key)
    visited[key] = True
    while not queue.is_empty():
        u = queue.dequeue()
        traversal_order.append(u)
        for _, v in graph._get_vertex(u).outgoing_edges():
            if not visited[v]:
                visited[v] = True
                queue.enqueue(v)
    return traversal_order


# Example usage
file_path = Path.cwd() / "asset" / "txt" / "graph_bfs_traverse.txt"
my_graph = Graph()
my_graph.read_file(file_path)
print(my_graph)

traversal = bfs_traverse(my_graph, 3)
print("BFS Traversal Order:", " -> ".join(map(str, traversal)))
# 3 -> 0 -> 2 -> 4 -> 1 -> 5 -> 6
