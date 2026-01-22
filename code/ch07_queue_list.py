class Queue:
    """FIFO Queue implementation using Python list"""
    
    def __init__(self):
        """Create an empty queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the queue."""
        return len(self._data)
    
    def __str__(self):
        """Return the string representation of the queue."""
        return "Front " + str(self._data) + " Back"
    
    def __repr__(self):
        """Return the string (internal) representation of the queue."""
        return f"Queue({'->'.join(map(str, self._data))})"
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue.
        Raise IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)
    
if __name__ == "__main__":
    # Example usage of the queue class.
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue)
    queue.enqueue("10")
    print(repr(queue))
    print(len(queue))