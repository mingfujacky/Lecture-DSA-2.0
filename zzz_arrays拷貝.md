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
  .small-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .small-grid img {
    width: 50%;
  }
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: LightSkyBlue;  
  }

  .small-text {
    font-size: 0.75rem;
  }
---
# What is Array
- Array is a data structure consisting of a collection of elements, of same memory size, each identified by an index. 
- Memory address of an element can be computed by 
  [array_start_address] + ([size] * [index])
<img src="asset/image/array_memory_address.png" width="800">

# Characteristics of Arrays
- Stores elements in contiguous memory 
  <span class="blue-text">=> array size must be known when creating (static array)</span>
- Elements are of the same data type
 <span class="blue-text"> => memory size of each element is the same => calculate address by formula => index-based access</span>
- Access element is O(1) due to index-based access
- Insertion and deletion is either O(1) or O(n) depending on shifting approach
  - Insertion or deletion at the end: O(1)
  - Insertion or deletion at the beginning or middle: O(n)
- Can be sorted or unsorted
- Can be static (fixed size) or dynamic (resizable)

# Are Lists Arrays?
- Lists aren’t arrays
  - Arrays have a fixed length and an unique type
  - Lists are dynamic and can store elements of different types
  - But, list is the typical go-to data type for Python programmers needing an array or array-like structure
- List doesn’t store actual values directly. Instead, it stores references (pointers) to objects in memory. That’s why lists can hold elements of different types and provide index-based access.
- a = [10, 20, 'GfG', 40, True]
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20250213130630102777/python-list.webp" width="300">

# How Lists Expand in Memory
- Python allocates some extra space in memory, such that we can add a few items to it.
- If we add enough items to the list, these spare locations will be used up, thus forcing Python to allocate a new space of memory and move all the pointers to that location. 
- Python does this for us automatically and behind the scenes
```python
import sys
my_list = []
for k in range(32):
    l = len(my_list)
    s = sys.getsizeof(my_list)
    print(f"Length: {l:3d}; Size in bytes: {s:4d}")
    my_list.append(None)
```

# Implement Unsorted Static Array by Python List
- insert function: insert an value at the end of the array
- delete function: delete an value at a given index, shift elements to the left
- find function: find the index of a given value 
<img src="asset/image/unsorted_static_array_class_diagram.png" width="400">
>[Code: Unsorted Static Array by List](code/ch03_unsorted_static_array.py)

# Implement Sorted Static Array by Python List
- insert function: insert an value at the correct position to maintain sorted order, shift elements to the right

>[Code: Sorted Static Array by List](code/ch03_sorted_static_array.py)

# Array Applications
- One dimensional array
- Greedy methods
- Two dimensional array
- Dynamic programming
- String manipulation
- String matching

>[Code: Array Applications](code/ch03_array_applications.ipynb)

# Supplement: Python Magic Methods
- Magic methods that start and end with double underscores are special methods in Python
- They allow you to define how objects of your class behave with built-in operations and functions.
- You can customize the behavior of your objects, such as arithmetic operations, comparisons, string representations, and more.

![bg right:50% w:60%](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff69d1d4d-91ac-409a-baa2-ccd4c4aaab13_1700x2087.png)

# \_\_str\_\_() vs \_\_repr\_\_()
Method | Purpose | When Used?
-------|---------|-----------
\_\_str\_\_()|Readable, user-friendly representation|print(obj), str(obj)
\_\_repr\_\_()|Developer-friendly, unambiguous representation (often used for debugging)| repr(obj), or print(obj) if \_\_str\_\_() is missing


# Homework DSA_HW_B