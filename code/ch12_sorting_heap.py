def heapify(arr, n, i):
    """
    To heapify a subtree rooted with node i.
    n is the size of the heap.
    """
    # Initialize largest as root
    largest = i

    # Left child index: 2 * i + 1
    left_child = 2 * i + 1

    # Right child index: 2 * i + 2
    right_child = 2 * i + 2

    # Check if left child of root exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child of root exists and is greater than the largest so far
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Change root if needed
    if largest != i:
        # Swap the root with the largest child
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Main function to sort an array of given size using Heap Sort.
    """
    n = len(arr)

    # Step 1: Build a Max Heap
    # We start from the last non-leaf node and heapify each node up to the root.
    # The last non-leaf node is at index (n // 2) - 1.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (the largest element) to the end of the array
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap to find the next largest element
        heapify(arr, i, 0)


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Original array:")
    print(data)

    heap_sort(data)
    print("\nSorted array:")
    print(data)
