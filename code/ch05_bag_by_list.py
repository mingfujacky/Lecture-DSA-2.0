class Bag:
    """
    ADT Bag implemented using Python list. Order of elements is not guaranteed.
    """

    def __init__(self, items=None):
        self._data = []
        if items is not None:
            for item in items:
                self._data.append(item)

    def insert(self, item):
        self._data.append(item)
        return True

    def remove(self, item):
        try:
            self._data.remove(item)
            return True
        except ValueError:
            return False

    def clear(self):
        self._data.clear()

    def get_current_size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def get_frequency_of(self, item):
        return self._data.count(item)

    def contains(self, item):
        return item in self._data

    def traverse(self):
        if self is not None:
            return " ".join(self._data)
        else:
            return "Bag is empty"

    def __str__(self):
        return f"{self._data}"

    def __repr__(self):
        return f"Bag(size={self.get_current_size()}, items={self._data})"


# -------------------------
# Quick demo
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
    print("After clear: empty?", b.is_empty())
