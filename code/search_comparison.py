import time

# Prepare a list of 1 million numbers
data = list(range(1_000_000))
target = 999_999  # The very last item

# --- Algorithm 1: Linear Search (Slow) ---
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# --- Algorithm 2: Binary Search (Fast) ---
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# --- Performance Test ---
print(f"Searching for {target} in 1,000,000 items...\n")

# Time Linear Search
start = time.perf_counter()
linear_search(data, target)
end = time.perf_counter()
print(f"Linear Search took: {(end - start):.6f} seconds")

# Time Binary Search
start = time.perf_counter()
binary_search(data, target)
end = time.perf_counter()
print(f"Binary Search took: {(end - start):.6f} seconds")
