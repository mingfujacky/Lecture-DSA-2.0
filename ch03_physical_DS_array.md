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
# Physical Data Structures
> Implement data structure in memory
<div class="grid">

<div>

![w:100% categories data structure](asset/image/physical_data_structure.jpg)

</div>

<div>

<span class="small-text">

> A **sequential storage structure** is a method of storing data elements in <span class='blue-text'>physically contiguous memory locations </span> where the logical order of the data is the same as the physical order in memory. The primary data structure used to implement this storage method is an <span class='blue-text'>array</span>.

</span>

</div>

</div>

# Implement Sequential Storage Structure by Referential Arrays
> Python represents a list or tuple instance by an array of object references.
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19]
temp = primes[3:6]
```
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*g-xoUeSW6mfdyh0LHKSXmw.png" width="400">

# Implement Sequential Storage Structure by Compact Arrays
> A compact array stores primary data instead of their references.
> Python represents a string or array.array instance by compact array.
```python
import array
myArray = array.array('i', [3, 5, 13, 2])
myString = "SAMPLE"
```
<img src = "asset/image/compact_array_addresses.jpg" width="800">


# Characteristics of Arrays
> Array is a data structure consisting of a collection of elements, of same memory size, each identified by an index. 
- Array size must be known when creating (by default static array)
- Stores elements in contiguous memory 
- Elements are of the same data type
- Each element can be accessed directly using its index
- Address of an element can be computed by [start_address] + ([index] * [size])
<img src="asset/image/array_memory_address.png" width="600">

# Static Array is Not Good Enough, How Come?
> Arrays are implemented as a <span class="red-text">contiguous block of memory</span>. Once a static array is full, require <span class="red-text">array expansion </span> to add more elements.
- A new, larger array must be created.
- Elements must be transferred from the old array to the new one.
<img src="asset/image/fix_size_array_full.png" width="300">

# Python Do Array Expansion Automatically
> The expansion process is handled internally, so you can treat the compact array (array.array) and referential array (list) as a dynamic array that can grow as needed.
```python
import array, sys
my_array = array.array('i')  # Create an empty array of integers
print(f"Length: {len(my_array)}, Size in bytes: {sys.getsizeof(my_array)}")

for i in range(1, 33):
    my_array.append(i)
    print(f"Length: {len(my_array)}, Size in bytes: {sys.getsizeof(my_array)}")
  
print(my_array)    
print('_' * 40, 'POP', '_' * 40)

print(f"Length: {len(my_array)}, Size in bytes: {sys.getsizeof(my_array)}")
for _ in range(32):
    my_array.pop()
    print(f"Length: {len(my_array)}, Size in bytes: {sys.getsizeof(my_array)}")
```

# Are Lists Arrays?
- In the traditional sense, a Python list is not a typical array. 
  - By default, arrays have a fixed length and an unique type
  - Lists are dynamic and can store elements of different types
  - But, list is a go-to data type for Python programmers needing an array structure
- List could be a referential array which doesn’t store actual values directly. Instead, it stores references (pointers) to objects in memory. That’s why lists can hold elements of different types and provide index-based access.
- a = [10, 20, 'GfG', 40, True]
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20250213130630102777/python-list.webp" width="300">

# Python Do List Expansion Automatically
> Similar to array expansion, Python lists automatically resize themselves when they run out of space.
```python
import sys
my_list = []
print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")

for i in range(1, 33):
    my_list.append(i)
    print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")
  
print(my_list)    
print('_' * 40, 'POP', '_' * 40)

print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")
for _ in range(32):
    my_list.pop()
    print(f"Length: {len(my_list)}, Size in bytes: {sys.getsizeof(my_list)}")
```

# Array Applications
[code/ch03_array_applications.ipynb](code/ch03_array_applications.ipynb)

# Recap
- Sequential storage structure stores data elements in physically contiguous memory locations.
- Arrays are a common implementation of sequential storage structures, characterized by fixed size, contiguous memory allocation, and direct indexing.
- Python lists and arrays automatically handle resizing, allowing for dynamic growth as needed.

# Review Questions
1. What is not a characteristic of a static array?
(a) Fixed memory size when created. 
(b) Elements stored in continuous memory addresses. 
(c) Can change its size dynamically. 
(d) All elements are of the same data type.

2. How to calculate the memory address of an element in an array?
(a) [start_address] + ([index] * [size])
(b) [start_address] + ([index] + [size])
(c) [start_address] * ([index] * [size])
(d) [start_address] * ([index] + [size])

# Homework DSA_HW_B
- 請完成下方所列的 Grind 75的題目，並於期限內繳交，請注意不受理逾期繳交 
- Submit program and output together with file name 學號_姓名_DSA_HW_B.zip
- Ensure the code is well-commented and test with multiple cases.
- Grind 75 (https://www.techinterviewhandbook.org/grind75/?grouping=topics)
  - Array # 1: Two Sum
  - Array # 2: Best Time to Buy and Sell Stock
  - Array # 3: Majority Element
  - Array # 4: Contains Duplicate
  - String # 1: Valid Palindrome
  - String # 2: Valid Anagram
  - String # 3: Longest Palindrome

