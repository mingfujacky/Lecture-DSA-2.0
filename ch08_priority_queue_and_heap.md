---
marp: true
theme: default
class: default
size: 16:9
paginate: true
header: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .columns img {
    width: 100%;
  }

  .middle-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 100%;
  }

  .red-text {
    color: red;
  }
  
  .blue-text {
    color: lightskyblue;  
  }

  .small-text {
    font-size: 0.50rem;
  }
---
# Priority Queues and Heaps
![bg right:50% w:90%](asset/image/priority_queue_concept.png)
- **Priority Queue** is a container that allows elements to be added or removed according to its priority.
- When a new element enters the priority queue, it’s not placed last. Its position is determined by its priority.
- An emergency room of a hospital or bug fixing list

# ADT: Priority Queue
Priority queue always return the element with the highest priority.
- insert(x, p): insert an element x having priority p into the priority queue
- top(): remove the highest-priority item from the priority queue and return it

<div class="columns">
    <img src="asset/image/priority_queue_diagram.png">
</div>

# Sorted Data Structures to Implement Priority Queue
- Sorted array
- Sorted linked list
- Insertion is O(n): go through the whole list
- Extracting the highest priority element is O(1): at the front of a linked list or at the end of an array.
<div class="middle-grid">
    <img src="asset/image/priority_queue_sorted_array.png">
    <img src="asset/image/priority_queue_sorted_linked_list.png">
</div>

# Unsorted Data Structures to Implement Priority Queue
- Unsorted array
- Unsorted linked list
- Insertion is O(1): at the front of a linked list or at the end of an array
- Extracting the highest priority element is O(n): go through the whole list.
<div class="middle-grid">
    <img src="asset/image/priority_queue_unsorted_array.png">
    <img src="asset/image/priority_queue_bigO_compare.png">
</div>
Can we have a balance between insert() and top()?

# Heap
A heap is a special kind of tree. It can be **binary heaps** or **d-way heaps** (heaps where nodes have more than two children)

<div class="middle-grid">
    <img src="asset/image/heap_structure.png">
    <img src="asset/image/min_heap_terminology.svg">
</div>

# Heap Properties
1. A binary heap, each node of the tree can have at most two children
2. Heap tree is “complete” or “almost complete”
   - Every level of the tree is complete, except the last level 
   - Nodes on the last level are as far left as possible (盡可能靠左)
3. each node holds the highest priority element in the subtree rooted at that node
<div class="middle-grid">
    <img src="asset/image/heap_complete.png">
    <img src="asset/image/heap_data.png">
</div>

# Heap Features
- Partial sort: all paths from the root to any leaf of the tree are sorted.
- Node number of each level: there are 2<sup>i</sup> nodes of level i. (i is the height, distance from the root).
<div class="middle-grid">
    <img src="asset/image/heap_partial_sort.png">
    <img src="asset/image/heap_node_number.png">
</div>

# Performance of Heap
Implementing insert and top operations only walk a path from the root to a leaf. This means that their running time is proportional to the height of the heap (log n).
![](asset/image/heap_Big_O.png)

# Max-heap and Min-heap
- A max-heap is a heap where each parent has a value no smaller than its children. priority(P) ≥ priority(C)
- Set a priority function to turn min-heap to max-heap because max-heap is more straight-forward, like f(x) = -x
<div class="middle-grid">
    <img src="asset/image/heap_max_min.png">
</div>

# Design a Heap
- We could implement a heap as a tree. But, we do not. We have a better way.
- The node with index 3. Its parent has index 1, and its children have indexes 7 and 8.
- Given a node with an index i > 0, its parent’s index is given by the integer division (i - 1) // 2, and its children have indexes 2 * i + 1 and 2 * i + 2
- Assuming the static array has enough space to store the elements and left-justified. 
<div class="middle-grid">
    <img src="asset/image/heap_index.png">
    <img src="asset/image/heap_array.png">
</div>

# Implement by List
[code/ch08_heap.py](code/ch08_heap.py)

# Lab of Heap Init and Helper Functions
```python
# uses an array (a Python list) as an internal attribute
class Heap:
    def __init__(self, elements=None element_priority=lambda x: x):
        self._priority = element_priority
        if elements is not None and len(elements) > 0:
            self._heapify(elements)
        else:
            self._elements = []

    def _has_lower_priority(self, element_1, element_2):
        return self._priority(element_1) < self._priority(element_2)
    
    def _has_higher_priority(self, element_1, element_2):
        return self._priority(element_1) > self._priority(element_2)
    
    def _left_child_index(self, index):
        return index * ? + 1
    
    def _parent_index(self, index):
        return (index - 1) ?? 2        
```
# Design Heap Insert (Bubble Up)

<div class="middle-grid">
    <img src="asset/image/heap_insert_1.png">
    <img src="asset/image/heap_insert_2.png">
</div>
<br>
<div class="middle-grid">
    <img src="asset/image/heap_insert_3.png">
    <img src="asset/image/heap_insert_4.png">
</div>

# Lab of Heap Insert
```python
def insert(self, element):
    self._elements.ap????(element)
    self._bubble_up(len(self._elements) - 1)

def _bubble_up(self, index):
    element = self._elements[index]
    while index > 0:
        parent_index = self._parent_index(index)
        parent = self._elements[parent_index]
        if self._has_higher_priority(el?????, parent):
        # There is a violation of the heap’s property, 
        # and we need to swap the new element with its parent
            self._elements[index] = parent
            index = parent_?????
        else:
        # The new element and its parent don’t violate the heap’s properties,
        #  so we have found the final place to insert the new element.    
            break
    self._elements[index] = element    
```

# Design Heap Top (Push Down)

<div class="middle-grid">
    <img src="asset/image/heap_top_1.png">
    <img src="asset/image/heap_top_2.png">
    <img src="asset/image/heap_top_3.png">
</div>

# Lab of Heap Top
```python
def top(self):
    if self.is_empty():
        raise ValueError('Method top called on an empty heap.')
    
    if len(self) == 1:
        # If the heap has a single element, we just need to pop its root.
        element = self._elements.pop()
    else:
        element = self._elements[0]
        self._elements[0] = self._elements.???()
        self._push_down(0)
    return element
```
# Lab of Heap Top Helper (_push_down)
```python
    def _push_down(self, index):
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
                current_index = ch???_index
            else:
                break

        self._elements[current_index] = element
```

# Lab of Heap Top Helper (_highest_priority_child_index)
```python
def _highest_priority_child_index(self, index):
    first_index = self._left_child_index(index)
    if first_index >= len(self):
        # The current node has no children.
    return None
    
    if first_index + 1 >= len(self):
    # The current node only has one child.
    return first_index

    if self._has_higher_priority(self._elements[first_index], self._elements[first_index + 1]):
        return first_index
    else:
        return first_index ? 1
```

# Design Heap Heapify

<div class="middle-grid">
    <img src="asset/image/heap_heapify_1.png">
    <img src="asset/image/heap_heapify_2.png">
    <img src="asset/image/heap_heapify_3.png">
</div>

# Implement Heap Heapipy
Takes O(n) comparison and assignments

```python
def _heapify(self, elements):
    self._elements = elements[:]
    last_inner_node_index = self._first_leaf_index() - 1
    for index in range(last_inner_node_index, -1, ??):
        self._push_down(index)

def _first_leaf_index(self):
    return len(self) // 2
```

# Calculate the First Leaf Index
Why the First Leaf is at n // 2?
For a heap with $n$ elements, the indices range from $0$ to $n-1$.
- The Last Node: The very last node in the heap is at index $n-1$.
- The Parent of the Last Node: Using the parent formula, the last node's parent is at index:
$$\text{Parent Index} = \lfloor ((n-1) - 1) / 2 \rfloor = \lfloor (n/2) - 1 \rfloor$$

- The First Leaf: Since the last internal node is $\lfloor (n/2) - 1 \rfloor$, the very next node in the array must be the first node that has no children.
$$\text{First Leaf Index} = \lfloor n/2 \rfloor$$

# Design 'Find the k Largest Entries'
![bg right:50% w:90%](asset/image/heap_find_k_largest_num.png)

Maintain a min-heap of the top k elements seen so far.
Iterate through all elements:
- If the heap has fewer than k elements → push it in.
- Else if the element is larger than the smallest (root) in the heap → pop the smallest and push the new one.

# Implement 'Find the k Largest Entries'
```python
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
            print('inserted', arr[i])
            print(heap)
    print(heap)        
    return heap.top()
# main
nums = [6, 5, 2, 1, 8, 7]
k = 3
print(k_largest_elements(nums, k))
```

# Recap
- A priority queue is an abstract data type that provides two operations: insert and top.
- Priority queues can be implemented using different data structures, but heap is the most efficient way.
- A binary heap is a special type of tree. It’s a binary, almost complete tree, where each node has a priority higher than or equal to its children’s.
- With the array implementation of a heap, we can build a priority queue where insert and top take O(log n) time.

# Review Questions
1.	What is the main purpose of a priority queue?
Priority queue（優先佇列）的主要目的為何？
(a)Store elements in insertion order 以插入順序儲存元素
(b)Always remove the most recently added element 永遠移除最新加入的元素
(c)Always remove the element with highest priority 永遠移除優先權最高的元素
(d)Remove elements at random 隨機移除元素

2.	Which of the following is a property of heaps? 
下列何者為 heap（堆積）的屬性？
(a)Each level must be sorted 每一層都必須排序
(b)Every subtree must be a full binary tree 每個子樹都必須是 full binary tree
(c)Every path from root to leaf is partially sorted 從根到葉的路徑具有部分排序性
(d)Each node must be greater than its siblings 每個節點皆比其兄弟節點大

