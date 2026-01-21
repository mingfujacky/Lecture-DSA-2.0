from ch04_singly_linked_list import SinglyLinkedList

class Bag:
    """
    ADT Bag implemented using singly linked list. Order of elements is not guaranteed"""

    def __init__(self, items=None):
        self._list = SinglyLinkedList()

        if items is not None:
            for item in items:
                self.insert(item)

    # -------- Insert / Remove / Clear --------
    def insert(self, item):
        self._list.insert_in_front(item)
        return True

    def remove(self, item):
        return self._list.delete(item)

    def clear(self):
        self._list._head = None

    # -------- Counting --------
    def get_current_size(self):
        return len(self._list)

    def is_empty(self):
        return self._list.is_empty()

    def get_frequency_of(self, item):
        count = 0
        current = self._list._head
        while current is not None:
            if current.data == item:
                count += 1
            current = current.next
        return count

    # -------- Query --------
    def contains(self, item):
        return self._list.search(item)

    def traverse(self, functor):
        if self.is_empty():
            return "Bag is empty"
        return " ".join(self._list.traverse(str))

    # -------- String --------
    def __str__(self):
        return f"{self._list.traverse(str)}"

    def __repr__(self):
        return f"Bag(size={self.get_current_size()}, items={self._list.traverse(str)})"


# -------------------------
# Quick demo (unchanged)
# -------------------------
if __name__ == "__main__":
    b = Bag(["Ace", "Ace", "King"])
    print("Init:", b)
    print(repr(b))

    b.insert("Queen")
    print("After add:", b)

    print("contains King?", b.contains("King"))
    print("freq(Ace):", b.get_frequency_of("Ace"))

    b.remove("Ace")
    print("After remove one Ace:", b)

    print("Traverse return:", b.traverse(str))

    b.clear()
    print("After clear: empty?", b.is_empty())
