def selection_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
