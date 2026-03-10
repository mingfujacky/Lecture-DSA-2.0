from ch03_unsorted_static_array import UnsortedStaticArray

class SortedStaticArray(UnsortedStaticArray):
    """
    SortedStaticArray
    ------------
    A fixed-capacity array implementation with type checking.
    Keep the elements sorted at all times.
    Features:
    - Fixed maximum size (no dynamic resizing)
    - Homogeneous element type (int / float / str)
    - Supports indexing, insertion, deletion (with shift), search, traversal
    """

    def __init__(self, max_size, typecode="int"):
        super().__init__(max_size, typecode)

    def insert(self, val):
        """
        Insert while maintaining sorted order

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
        
        pos = 0
        while pos < self._size and self._array[pos] < val:
            pos += 1

        # Shift elements to the right to make space
        for i in range(self._size, pos, -1):
            self._array[i] = self._array[i - 1]

        self._array[pos] = val
        self._size += 1

if __name__ == "__main__":
    a = SortedStaticArray(5, "int")  # _init__
    a.insert(0)
    a.insert(7)
    a.insert(-1)
    a.insert(3)
    print(a)  # __str__
    print(repr(a))  # __repr__