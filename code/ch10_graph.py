from ch06_stack_list import Stack
from ch07_queue_list import Queue
from ch10_graph_vertex import Vertex
from pathlib import Path

class Graph:
    def __init__(self):
        self._vertex_number = 0
        self._edge_number = 0
        self._adj = {}
    
    def __repr__(self):
        def edges_repr(edges):
            return f"[{', '.join((f'->{u}' for (_, u) in edges))}]"

        adj_lst_repr = (f'{repr(v)}: {edges_repr(v.outgoing_edges())}' for v in self._adj.values())
        return f'Graph({" | ".join(adj_lst_repr)})'
    
    def read_file(self,file_name):
        with open(file_name, 'r') as f:
            self._vertex_number, self._edge_number = map(int, f.readline().split())
            for k in range(self._vertex_number):
                self._adj[k] = Vertex(k)
            for _ in range(self._edge_number):
                i, j = map(int,f.readline().split())
                self._adj[i].add_edge_to(self._adj[j])

    def __str__(self):	
        result = []
        for key in self._adj:
          result.append(f"{key}: {self._adj[key].outgoing_edges()}")
        return "\n".join(result)


    def _get_vertex(self, key):
        if key not in self._adj:
            raise ValueError(f'Vertex {key} does not exist!')
        return self._adj[key]

    def insert_vertex(self, key):
        """Add a vertex to the graph with the given key."""
        if key in self._adj:
            raise ValueError(f'Vertex {key} already exists!')
        self._adj[key] = Vertex(key)
        self._vertex_number += 1

    def has_vertex(self, key):
        """Check if the graph contains a vertex with the given key."""
        return key in self._adj
    
    def delete_vertex(self, key):
        """Delete a vertex from the graph. Also removes all edges connected to it."""
        v = self._get_vertex(key)
        for u in self._adj.values():
            if u != v and u.has_edge_to(v):
                u.delete_edge_from(v)
        del self._adj[key]
        self._vertex_number -= 1

    def get_vertices(self):
        """Get a list of the unique identifiers of all vertices in the graph."""
        return set(self._adj.keys())
    
    def vertex_count(self):
        """Get the number of vertices in the graph."""
        return len(self._adj)
    
    def insert_edge(self, key1, key2):
        """Add an edge between two vertices in the graph."""
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.add_edge_to(v2)
        self._edge_number += 1

    def has_edge(self, key1, key2):
        """Check if the graph contains an edge between two vertices."""
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        return v1.has_edge_to(v2)
    
    def delete_edge(self, key1, key2):
        """Delete an edge between two vertices in the graph."""
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.delete_edge_from(v2)
        self._edge_number -= 1

    def get_edges(self):
        """Get a list of all edges in the graph."""
        return set(e for v in self._adj.values() for e in v.outgoing_edges())

    def edge_count(self):
        """Get the number of edges in the graph."""
        return sum(len(v.outgoing_edges()) for v in self._adj.values())
    
    def bfs_traverse(self, start_vertex):
        """Perform a breadth-first traversal from a given vertex."""
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')

        visited = {v: False for v in self._adj}
        queue = Queue()
        traversal_order = []

        queue.enqueue(start_vertex)
        visited[start_vertex] = True

        while not queue.is_empty():
            u = queue.dequeue()
            traversal_order.append(u)

            for (_, v) in self._get_vertex(u).outgoing_edges():
                if not visited[v]:
                    visited[v] = True
                    queue.enqueue(v)

        return traversal_order
    
    def bfs_shortest_path(self, start_vertex, target_vertex):
        """Perform a breadth-first search from a given vertex. Looks for the shortest path from the start vertex to the target vertex."""
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')
        if not self.has_vertex(target_vertex):
            raise ValueError(f'Target vertex {target_vertex} does not exist!')

        def reconstruct_path(pred, target):
            # Reconstruct the path from start to target by going back until it finds a vertex without predecessor: That can only be the start vertex
            path = []
            while target:
                path.append(target)
                target = pred[target]
            return path[::-1]

        distance = {v: float('inf') for v in self._adj}
        predecessor = {v: None for v in self._adj}

        queue = Queue()
        # Initially, we add the start vertex to the queue
        queue.enqueue(start_vertex)
        distance[start_vertex] = 0

        while not queue.is_empty():
            u = queue.dequeue()
            if u == target_vertex:
                # We have found the shortest path to the target
                return reconstruct_path(predecessor, target_vertex)

            # For each of u's neighbors, we check if there was already a shorter path to them
            for (_, v) in self._get_vertex(u).outgoing_edges():
                if distance[v] == float('inf'):
                    distance[v] = distance[u] + 1
                    predecessor[v] = u
                    queue.enqueue(v)

        #At this point, we know there is no path from the start to the target vertex
        return None

    def dfs(self, start_vertex, color = None):
        """Perform a depth-first search from a given vertex. Looks for the shortest path from the start vertex to the target vertex.

        Parameters:
            start_vertex: The unique identifier of the start vertex.
            color: A dictionary mapping vertices to colors. If not provided, a new dictionary is created.

        Returns:
            Tuple[bool, dict]: A tuple containing a boolean indicating whether the graph is acyclic, and the up-to-date dictionary mapping vertices to colors.
        """
        
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')
        if color is None:
            color = {v: 'white' for v in self._adj}
        acyclic = True
        stack = Stack()
        stack.push((False, start_vertex))
        while not stack.is_empty():
            (mark_as_black, v) = stack.pop()
            col = color.get(v, 'white')
            if mark_as_black:
                color[v] = 'black'
            elif col == 'grey':
                acyclic = False
            elif col == 'white':
                color[v] = 'grey'
                stack.push((True, v))
                for (_, w) in self._get_vertex(v).outgoing_edges():
                    stack.push((False, w))
        return acyclic, color

if __name__ == "__main__":
    # Example usage of the Graph class.
    graph = Graph()
    for key in range(1, 6):
        graph.insert_vertex(key)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 1)
    graph.insert_edge(2, 4)
    graph.insert_edge(3, 1)
    graph.insert_edge(3, 4)
    graph.insert_edge(4, 2)
    graph.insert_edge(4, 3)
    graph.insert_edge(4, 5)
    graph.insert_edge(5, 4)
    print(graph)

    print("BFS Traversal from 1:", graph.bfs_traverse(1))

    print("BFS from 1 to 4:", graph.bfs_shortest_path(1, 4))

    acyclic, color_map = graph.dfs(1)
    print("DFS from 1 - Acyclic:", acyclic)
    print("Vertex colors after DFS:", color_map)

    # Example of reading a graph from a file
    file_path = Path.cwd() / 'asset' / 'txt' / 'graph_star.txt'
    graph_from_file = Graph()
    graph_from_file.read_file(file_path)
    print(graph_from_file)
    


