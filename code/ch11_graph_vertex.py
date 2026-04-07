class Vertex:
    def __init__(self, key):
        self._key = key
        self._adjacency_list = []

    def __eq__(self, other):
            return self._key == other._key
    
    def __str__(self) -> str:
        return f'<{str(self._key)}>'
    
    def __repr__(self):
        return f"Vertex({self._key})"    

    def add_edge_to(self, destination_vertex):
        """Add an edge from this vertex to the destination vertex."""
        if self.has_edge_to(destination_vertex):
            raise ValueError(f'Edge already exists: {self} -> {destination_vertex}')
        self._adjacency_list.append(destination_vertex)        
    
    def has_edge_to(self, destination_vertex):
        """Check if there is an edge from this vertex to the destination vertex."""
        return (destination_vertex in self._adjacency_list)      
    
    def delete_edge_from(self, destination_vertex):
        """Remove the edge from this vertex to the destination vertex, if it exists."""
        if not self.has_edge_to(destination_vertex):
            raise ValueError(f'Edge does not exist: {self} -> {destination_vertex}')
        self._adjacency_list.remove(destination_vertex)

    def outgoing_edges(self):
        """Get a list of outgoing edges from this vertex."""
        return [(self._key, v._key) for v in self._adjacency_list]    
    
if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)

    v1.add_edge_to(v2)
    v1.add_edge_to(v3)
    v2.add_edge_to(v4)
    print(v1 == v2)
    print(v1)
    print(v1.outgoing_edges())
    
    print(v1.has_edge_to(v2))
    print(v2.has_edge_to(v3))
    v1.delete_edge_from(v2)
    print(v1.outgoing_edges())