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

>A **linked storage structure** is a storage structure that <span class='blue-text'>uses references (links or pointers) to connect individual data records (nodes)</span>, rather than storing them in contiguous memory locations like an array. Each node contains both the data itself and a link to the next node in the sequence. The primary data structure used to implement this storage method is an <span class='blue-text'>linked list</span>.

</span>

</div>

</div>

# Implement Linked Storage Structure by Linked Lists
- A linked list is a linear data structure where each node contains a data part and a link to the next node. 
- The nodes are not stored in contiguous memory locations; instead, they are linked together using links (pointers).
- Node 3 -> 5 -> 13 -> 2

![bg right 60% w 95%](asset/image/linked_list_memory_address.jpg)

# Compare Linked List and Array
- Array elements are stored in contiguous memory. Linked list nodes are not stored contiguously.
- Linked list don't need allocate space in advance and copy data when add elements
- Linked list has no direct indexing
- Access an element in array and linked list is O(1) and O(n), respectively
- Insert an element in array and linked list is O(n) and O(1), respectively
- Delete an element in array and linked list is O(n) and O(1), respectively
<img src="asset/image/linked_list_vs_array.png" width="400">

# Implement Linked List Node
<img src="asset/image/linked_list_node_implementation.png" width="300">

```python
class Node:
    def __init__(self, data, next_node = None):
        self._data = data; self._next = next_node
    
    def data(self): return self._data

    def next(self): return self._next

    def has_next(self): return self._next is not None

    def append(self, next_node): self._next = next_node

    def __str__(self): return str(self.data())

    def __repr__(self): return f"Node(value: {repr(self._data)}, {id(self)}, next: {id(self._next) if self._next else None})"        

node1 = Node(1); node2 = Node(2); node3 = Node(3)
node1.append(node2); node2.append(node3)
print(repr(node1)); print(repr(node2)); print(repr(node3))  
print(node1)
```

