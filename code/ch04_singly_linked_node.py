class SinglyLinkedNode:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    @property
    def data(self):
        """Allows access to data via 'node.data' instead of 'node.data()'."""
        return self._data

    @property
    def next(self):
        """Allows access to the next node via 'node.next'."""
        return self._next

    def append(self, next_node):
        """Explicitly assigns the next node in the sequence."""
        self._next = next_node

    def __str__(self):
        """String representation of the data value."""
        return str(self._data)

    def __repr__(self):
        """Detailed view showing memory addresses for lecture debugging."""
        next_id = id(self._next) if self._next else None
        return f"Singly Linked List Node(data: {self._data}, id: {id(self)}, next node id: {next_id})"

    def traverse(self):
        """Prints the chain starting from this node."""
        current = self
        elements = []
        while current:
            elements.append(str(current.data))  # Note: using the @property here
            current = current.next  # Note: using the @property here
        print(" -> ".join(elements) + " -> None")


# --- Demo for Lecture ---
node1 = SinglyLinkedNode(100)
node2 = SinglyLinkedNode(200)

# Linking using the explicit append function
node1.append(node2)

print(f"Node 1 data: {node1.data}")  # Accessing like a variable, not a function
print(f"Node 1 next node address: {id(node1.next)}")
print("Traversal:")
node1.traverse()
print(node1)
print(repr(node1))
