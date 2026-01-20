from ch04_singly_linked_node import SinglyLinkedNode as Node

class SinglyLinkedList:
    """
    This class models a singly-linked list data structure and have insertion, deletion, search and traversal functions.
    """

    def __init__(self):  # _head: The head node of the list. Initialized to None.
        self._head = None

    def traverse(self, functor):
        # Traverse the linked list to put data into a list after applying functor to each node's data.
        current = self._head
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):  # Return the length of the linked list.
        return len(self.traverse(lambda x: x))

    def __repr__(self):
        return f'SinglyLinkedList({"->".join(self.traverse(repr))})'

    def __str__(self):
        return "->".join(self.traverse(str))

    def is_empty(self):
        return self._head is None

    def insert_in_front(self, data):  # Add a node to the beginning of the list.
        old_head = self._head
        self._head = Node(data, old_head)

    def insert_to_back(self, data):  # Append a node to the end of the list.
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))

    def get(self, index):  # Get the data at the given index.
        # Get the data at the given index.
        if index < 0:
            raise IndexError("Index must be non-negative")
        if index > len(self) - 1:
            raise IndexError("Index out of bounds")
        if self._head is None:
            raise IndexError("Empty Linked List")
    
        current = self._head
        current_index = 0
        while current_index < index and current is not None:
            current = current.next()
            current_index += 1
        
        if current is None:
            raise IndexError("Index out of bounds")
    
        return current.data()


    def search(self, target):
        # Search the list for a node with the data matching `target`.
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):  
        # Delete the first node with the given data from the list.
        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(
            f"No element with value {target} was found."
        )  # If get here, no found

    def delete_from_front(self):  # Delete the first node
        if self.is_empty():
            raise ValueError('Delete on an empty list.')
        data = self._head.data()
        self._head = self._head.next()
        return data

if __name__ == "__main__":
    foo = SinglyLinkedList()
    foo.insert_in_front(1)
    foo.insert_in_front(2)
    foo.insert_in_front(0)
    print(foo)
    print(foo.get(1))
    print(foo.delete_from_front())
    print(foo)

    boo = SinglyLinkedList()
    boo.insert_in_front(100)
    boo.insert_in_front(200)
    print(boo)

    foo.concatenate(boo)
    print(foo)

