from ch04_singly_linked_node import SinglyLinkedNode as Node

class Bag:
    """
    ADT Bag implemented using singly linked node. Order of elements is not guaranteed.
    """

    def __init__(self, items=None):
        self._head = None
        self._size = 0

        if items is not None:
            for item in items:
                self.insert(item)

    # -------------------------
    # Insert / Remove / Clear
    # -------------------------
    def insert(self, item):
        """Insert item into bag (at head). O(1)"""
        new_node = Node(item, self._head)
        self._head = new_node
        self._size += 1
        return True

    def remove(self, item):
        prev = None
        curr = self._head

        while curr is not None:
            if curr.data == item:
                if prev is None:
                    # removing head
                    self._head = curr.next
                else:
                    prev.next = curr.next
                self._size -= 1
                return True

            prev = curr
            curr = curr.next

        return False

    def clear(self):
        """Remove all items. O(1)"""
        self._head = None
        self._size = 0

    # -------------------------
    # Counting
    # -------------------------
    def get_current_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_frequency_of(self, item):
        count = 0
        curr = self._head
        while curr is not None:
            if curr.data == item:
                count += 1
            curr = curr.next
        return count

    # -------------------------
    # Query
    # -------------------------
    def contains(self, item):
        curr = self._head
        while curr is not None:
            if curr.data == item:
                return True
            curr = curr.next
        return False

    def traverse(self):
        if self.is_empty():
            return 'Bag is empty'

        result = []
        curr = self._head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next

        return ' '.join(result)

    # -------------------------
    # Python helper methods
    # -------------------------
    def __str__(self):
        items = []
        curr = self._head
        while curr is not None:
            items.append(curr.data)
            curr = curr.next
        return f"{items}"

    def __repr__(self):
        return f"Bag(size={self.get_current_size()}, items={self.__str__()})"


# -------------------------
# Quick demo (unchanged)
# -------------------------
if __name__ == "__main__":
    b = Bag(["Ace", "Ace", "King"])
    print("Init:", b)

    b.insert("Queen")
    print("After add:", b)

    print("contains King?", b.contains("King"))
    print("freq(Ace):", b.get_frequency_of("Ace"))
 
    b.remove("Ace")
    print("After remove one Ace:", b)

    print("Traverse return:", b.traverse())

    b.clear()
    print("After clear:", b, "empty?", b.is_empty())