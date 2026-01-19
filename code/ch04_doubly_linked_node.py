class DoublyLinkedNode:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"DoublyLinkedNode(data:{self._data}, id:{id(self)}, previous node id:{id(self._prev) if self._prev else None}, next node id:{id(self._next) if self._next else None})"

    def append(self, next_node):  # append a node to the current one
        self._next = next_node
        if next_node is not None:
            next_node._prev = self

    def prepend(self, prev_node):  # prepend a node to the current one.
        self._prev = prev_node
        if prev_node is not None:
            prev_node._next = self

    def traverse(self):
        current = self
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" None <- " + " <-> ".join(elements) + " -> None")


if __name__ == "__main__":
    # Example usage of the DoublyLinkedNode class
    node1 = DoublyLinkedNode(100)
    node2 = DoublyLinkedNode(200)
    node3 = DoublyLinkedNode(300)
    node1.append(node2)  # Link node1 to node2
    node3.prepend(node2)  # Link node3 back to node2
    print(f"Node 1 data: {node1.data}")  # Accessing like a variable, not a function
    print(repr(node1))
    print(f"Node 1 next node address: {id(node1.next)}")
    print(f"Node 2 prev node address: {id(node2.prev)}")
    print("Traversal:")
    node1.traverse()
