def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Calculate the position using interpolation formula
        pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))

        # Check if the target is found
        if pos < low or pos > high:
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Example usage
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Array:", arr)
    target = 70
    result = interpolation_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index: {result}")
    else:
        print(f"Element {target} not found in the array.")
