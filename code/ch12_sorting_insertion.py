def insertion_sort(arr):
    # Traverse from the second element to the last
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)
