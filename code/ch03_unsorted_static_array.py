class UnsortedStaticArray:
    """
    UnsortedStaticArray
    ------------
    A fixed-capacity array implementation with type checking.

    Features:
    - Fixed maximum size (no dynamic resizing)
    - Homogeneous element type (int / float / str)
    - Supports indexing, insertion, deletion (with shift), search, traversal
    """

    def __init__(self, max_size, typecode="int"):
        """
        Initialize a static array.

        Parameters:
        - max_size: maximum number of elements the array can hold
        - typecode: element type ("int", "float", or "str")
        """

        # Validate array capacity
        if max_size <= 0:
            raise ValueError(f"Invalid array size (must be positive): {max_size}")

        # Map typecode (string) to actual Python type
        _ALLOWED = {"int": int, "float": float, "str": str}
        self._type = _ALLOWED.get(typecode)

        # Reject unsupported element types
        if self._type is None:
            raise TypeError(f"Invalid array typecode, {typecode}")

        # Internal state
        self._typecode = typecode  # store original type name (for messages)
        self._max_size = max_size  # fixed capacity
        self._size = 0  # current number of stored elements
        self._array = [None] * max_size  # underlying storage

    @property
    def max_size(self):
        """Return the maximum capacity of the static array."""
        return self._max_size

    def __len__(self):
        """Return the number of elements currently stored in the array."""
        return self._size

    def __getitem__(self, index):
        """
        Retrieve element at the given index.

        Raises:
        - IndexError if index is out of valid range [0, size-1]
        """
        if index < 0 or index >= self._size:
            raise IndexError("array index out of range")
        return self._array[index]

    def __setitem__(self, index, val):
        """
        Assign a value to an existing index.

        Note:
        - Only indices < current size are allowed
        - This method does NOT resize the array
        """
        if index < 0 or index >= self._size:
            raise IndexError("array assignment index out of range")

        # Enforce homogeneous element type
        if not isinstance(val, self._type):
            raise TypeError(
                f"Expected value of type {self._typecode}, got {type(val).__name__}"
            )

        self._array[index] = val

    def insert(self, val):
        """
        Insert an element at the end of the array.

        Raises:
        - ValueError if the array is already full
        - TypeError if the value type is incorrect
        """
        if self._size >= self._max_size:
            raise ValueError("The array is already full")
        elif not isinstance(val, self._type):
            raise TypeError(
                f"Expected value of type {self._typecode}, got {type(val).__name__}"
            )

        # Insert at the first unused position
        self._array[self._size] = val
        self._size += 1

    def delete(self, index):
        """
        Delete the element at the given index.

        Implementation:
        - Shift all subsequent elements one position to the left
        - Preserves element order (stable delete)

        Time Complexity: O(n)
        """
        if self._size == 0:
            raise ValueError("Delete from an empty array")
        if index < 0 or index >= self._size:
            raise IndexError("array index out of range")

        # Shift elements left to fill the gap
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        # Clear last slot and update size
        self._array[self._size - 1] = None
        self._size -= 1

    def find(self, target):
        """
        Linear search for target value.

        Returns:
        - index if found
        - -1 if not found
        """
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return -1

    def traverse(self, callback):
        """
        Apply a callback function to each element in the array.

        Example:
        - traverse(print)
        - traverse(lambda x: ...)
        """
        for index in range(self._size):
            callback(self._array[index])

    def __repr__(self):
        """
        Developer-friendly representation:
        shows size, capacity, and active elements
        """
        return (
            f"UnsortedStaticArray(size={self._size}, "
            f"max_size={self._max_size}, "
            f"data={self._array[:self._size]!r})"
        )

    def __str__(self):
        """
        User-friendly string representation:
        shows only active elements
        """
        return str(self._array[: self._size])


if __name__ == "__main__":
    a = UnsortedStaticArray(5, "int")  # _init__
    # b = UnsortedStaticArray(-1, "int")  # _init__
    # c = UnsortedStaticArray(5, "complex")  # _init__
    #     print(a.max_size)
    #     print(len(a))  # __len__

    a.insert(0)
    a.insert(7)
    a.insert(-1)
    a.insert(3)

    a[0] = 2  # __setitem__
    #     print(a[0])  # __getitem__
    print(a)  # __str__
    print(repr(a))  # __repr__

    # delete method
    print("Delete:")
    a.delete(1)  # delete index 1, its value is 7
    print(repr(a))
    print()

    # find method
    print("Find:")
    print("index:", a.find(3))  # find value 3
    print("index:", a.find(10))  # find value 10
    print()

    # traverse method
    print("Traverse:")
    a.traverse(print)
    a.traverse(lambda x: print(x, end=" "))
