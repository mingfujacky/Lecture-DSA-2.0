class Heap:
    """Implementation of a binary heap. The heap is a max-heap.
    Uses an array (simulated by a Python list) as an internal attribute
    The priority of an element can be computed using a function passed as an argument to the constructor.
    """

    def __init__(self, elements=None, element_priority=lambda x: x):
        """
        elements: The elements for initializing the heap. By default, the heap is empty.
        element_priority: A function that extracts the priority of an element.
                          By default, the priority is the element itself.
        """
        self._priority = element_priority
        if elements is not None and len(elements) > 0:
            self._heapify(elements)
        else:
            self._elements = []

    def __len__(self):
        return len(self._elements)

    def _has_lower_priority(self, element_1, element_2):
        """Checks if the first element has lower priority to the second element."""
        return self._priority(element_1) < self._priority(element_2)

    def _has_higher_priority(self, element_1, element_2):
        """Checks if the first element has higher priority to the second element."""
        return self._priority(element_1) > self._priority(element_2)

    # def _validate(self):
    #     """Checks that the three properties for heaps are abided by.
    #     1.	Every node has at most 2 children.
    #     2.	The heap tree is almost-complete and left-adjusted.
    #     3.	Every node holds the highest priority in the subtree rooted at that node.
    #     """
    #     current_index = 0
    #     first_leaf = self._first_leaf_index()
    #     while current_index < first_leaf:
    #         current_element = self._elements[current_index]
    #         first_child = self._left_child_index(current_index)
    #         last_child_guard = min(first_child + 2, len(self))
    #         for child_index in range(first_child, last_child_guard):
    #             if self._has_lower_priority(
    #                 current_element, self._elements[child_index]
    #             ):
    #                 return False
    #         current_index += 1
    #     return True

    def _left_child_index(self, index):
        # Computes the index of the left child of a heap node.
        return index * 2 + 1

    def _parent_index(self, index):
        # Computes the index of the parent of a heap node.
        return (index - 1) // 2

    def _highest_priority_child_index(self, index):
        """Finds, among the children of a heap node, the one child with highest priority.
        In case multiple children have the same priority, the left-most is returned.

        Args:
            index: The index of the heap node whose children are searched.

        Returns: The index of the child of current heap node with highest priority,
                 or None if current node has no child.
        """
        first_index = self._left_child_index(index)

        if first_index >= len(self):
            # The current element has no children
            return None

        if first_index + 1 >= len(self):
            # The current element only has one child
            return first_index

        if self._has_higher_priority(
            self._elements[first_index], self._elements[first_index + 1]
        ):
            return first_index
        else:
            return first_index + 1

    def _first_leaf_index(self):
        """Computes the index of the first leaf of the heap.
        A leaf is the first node that has no children.
        For a binary heap, we know that's exactly the node in the middle of the array.
        """
        return len(self) // 2

    def _push_down(self, index):
        """Pushes down the root of a sub-heap towards its leaves to reinstate heap invariants.
        If any of the children of the element has a higher priority, then it swaps current
        element with its highest-priority child C, and recursively checks the sub-heap previously
        rooted at that C.

        Args:
            index: The index of the root of the sub-heap.
        """

        # INVARIANT: 0 <= index < n
        if not (0 <= index < len(self._elements)):
            raise IndexError("Out of range of the heap")
        element = self._elements[index]
        current_index = index
        while True:
            child_index = self._highest_priority_child_index(current_index)
            if child_index is None:
                break
            if self._has_lower_priority(element, self._elements[child_index]):
                self._elements[current_index] = self._elements[child_index]
                current_index = child_index
            else:
                break

        self._elements[current_index] = element

    def _bubble_up(self, index):
        """Bubbles up towards the root an element, to reinstate heap's invariants.
        If the parent P of the element (_elements[index]) has lower priority, then swaps the element and its parent,
        and then recursively check the position previously held by the P.

        Args:
            index: The index of the element to bubble up.
        """
        # INVARIANT: 0 <= index < n
        if not (0 <= index < len(self._elements)):
            raise IndexError("Out of range of the heap")
        element = self._elements[index]
        while index > 0:
            parent_index = self._parent_index(index)
            parent = self._elements[parent_index]
            if self._has_higher_priority(element, parent):
                self._elements[index] = parent
                index = parent_index
            else:
                break

        self._elements[index] = element

    def _heapify(self, elements):
        """Initializes the heap with a list of elements and priorities.

        Args:
            elements: The list of elements to add to the heap.
            priorities: The priorities for those elements (in the same order they are presented).
        """
        self._elements = elements[:]
        last_inner_node_index = self._first_leaf_index() - 1
        for index in range(last_inner_node_index, -1, -1):
            self._push_down(index)

    def is_empty(self):
        return len(self) == 0

    def top(self):
        """Removes and returns the highest-priority element in the heap.
        If the heap is empty, raises a `ValueError`.

        Returns: The element with highest priority in the heap.
        """
        if self.is_empty():
            raise ValueError("Method top called on an empty heap.")

        if len(self) == 1:
            element = self._elements.pop()
        else:
            element = self._elements[0]
            self._elements[0] = self._elements.pop()
            self._push_down(0)

        return element

    def peek(self):
        if self.is_empty():
            raise ValueError("Method peek called on an empty heap.")
        return self._elements[0]

    def insert(self, element):
        """
        Add a new element/priority pair to the heap
        element: The new element to add.
        """
        self._elements.append(element)
        self._bubble_up(
            len(self._elements) - 1
        )  # index of the new insert element is the last one

    def __str__(self):
        """Returns a string representation of the heap."""
        return "Heap:" + str(self._elements)

    def __repr__(self):
        if self.is_empty():
            return "Heap is empty"

        result = ""
        height = 0
        level_start = 0
        level_size = 1

        while level_start < len(self._elements):
            level_end = level_start + level_size
            level = self._elements[level_start:level_end]
            result += (
                "Level " + str(height) + " ⮕ " + " ".join(str(x) for x in level) + "\n"
            )
            height += 1
            level_start = level_end
            level_size *= 2  # next level has twice the number of nodes

        return result.strip()


if __name__ == "__main__":
    # Example usage
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.insert(7)
    print(heap)
    print(repr(heap))
    print(heap.top())  # Output: 8
    print(repr(heap))
    print(heap.peek())  # Output: 8
    print("length:", len(heap))

    foo = Heap([9, 4, 1, 3, 7, 8, 2, 6, 5])
    print(repr(foo))
    print("length:", len(foo))
    print(foo.top())  # Output: 9
    print(foo)

    foo = Heap([9, 4, 1, 3, 7, 8, 2, 6, 5])
    print('list = ', '[9, 4, 1, 3, 7, 8, 2, 6, 5]')
    print(repr(foo))

    print('list = ', '[9, 8, 7, 6, 5, 4, 3, 2, 1]')
    foo = Heap([9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(repr(foo))

    print('list = ', '[1, 2, 3, 4, 5, 6, 7, 8, 9]')
    foo = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(repr(foo))
    
    print()
    boo = Heap([9, 4, 1, 3, 7, 8, 2, 6, 5], lambda x: -x)
    print(repr(boo))
