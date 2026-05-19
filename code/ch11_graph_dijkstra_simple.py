import heapq


def dijkstra(graph, start):
    # Initialize distances
    shortest_paths = {vertex: float("inf") for vertex in graph}
    shortest_paths[start] = 0
    # To reconstruct the path, we can keep track of predecessors
    predecessors = {vertex: None for vertex in graph}
    # Priority queue to explore the vertices with the smallest distance first
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can only be added once to the priority queue, so we check if the distance is already greater than the recorded distance
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, predecessors


def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()  # Reverse the path to get the correct order
    if path[0] == start:
        return path
    else:
        return []  # No path found


graph = {
    "A": {"B": 4, "C": 5},
    "B": {"A": 4, "C": 11, "D": 9, "E": 7},
    "C": {"A": 5, "B": 11, "E": 3},
    "D": {"B": 9, "E": 13, "F": 2},
    "E": {"B": 7, "C": 3, "D": 13, "F": 6},
    "F": {"D": 2, "E": 6},
}
shortest_paths, predecessors = dijkstra(graph, "A")
print("Shortest paths from A:", shortest_paths)
for vertex, distance in shortest_paths.items():
    print(f"A to {vertex}: {distance}")
print("Predecessors:", predecessors)
for vertex, predecessor in predecessors.items():
    print(f"Predecessor of {vertex}: {predecessor}")

# Example of reconstructing a path
print("Path from A to F:", reconstruct_path(predecessors, "A", "F"))
