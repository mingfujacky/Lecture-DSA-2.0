"""Module providing an implementation for stack, using singly-linked lists to store the elements."""

from ch08_heap import Heap


def k_largest_elements(arr, k):
    heap = Heap(element_priority=lambda x: -x)
    for i in range(len(arr)):
        if len(heap) >= k:
            if heap.peek() < arr[i]:
                heap.top()
                heap.insert(arr[i])
                print(heap)
        else:
            heap.insert(arr[i])
            print("inserted", arr[i])
            print(heap)
    print(heap)
    return heap.top()


# main
nums = [6, 5, 2, 1, 8, 7]
k = 3
print(k_largest_elements(nums, k))
