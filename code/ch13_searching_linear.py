def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
if __name__ == "__main__":
    my_list = [5, 3, 2, 8, 1]
    target_value = 2
    result = linear_search(my_list, target_value)

    if result != -1:
        print(f"Element {target_value} found at index: {result}")
    else:
        print(f"Element {target_value} not found in the list.")
