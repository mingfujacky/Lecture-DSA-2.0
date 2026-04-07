from ch10_graph import Graph
from ch06_stack_list import Stack
from pathlib import Path


def dfs_traverse(graph, key):
    """Perform a depth-first traversal from a given vertex."""
    if isinstance(key, str) and key.isdigit():
        key = int(key)
    if not graph.has_vertex(key):
        raise ValueError(f"Start vertex {key} does not exist!")

    print(f"Starting DFS traversal from vertex: {key}")
    visited = {v: False for v in graph._adj}
    stack = Stack()
    traversal_order = []

    stack.push(key)
    while not stack.is_empty():
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            traversal_order.append(u)
            for _, v in graph._get_vertex(u).outgoing_edges():
                if not visited[v]:
                    stack.push(v)
    return traversal_order


# Example usage
file_path = Path.cwd() / "asset" / "txt" / "graph_dfs_traverse.txt"
my_graph = Graph()
my_graph.read_file(file_path)
print(my_graph)

traversal = dfs_traverse(my_graph, 3)
print("DFS Traversal Order:", " -> ".join(map(str, traversal)))
# 3 -> 0 -> 2 -> 1 -> 5 -> 4 -> 6
