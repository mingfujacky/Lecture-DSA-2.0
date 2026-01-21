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

# Design Singly Linked Node
![bg right 10% w 80%](asset/image/singly_linked_node_diagram.jpg)

# Implement Singly Linked Node
[ch04_singly_linked_node.py](code/ch04_singly_linked_node.py)

# Singly Linked List (SLL)
<div class="columns">
    <img src="asset/image/singly_linked_list_intro.png">
</div>

- Head node
  - First element of a linked list, no other node points to it
  - Use a variable point to the head node
- Tail node
  - Last element of the list, not point to next node, point to Null (None)
- Each node only knows its successor

# Design SLL
![bg right 40% w 80%](asset/image/singly_linked_list_diagram.jpg)
- Do not need specify a initial size
- Do not need same data type
- Insert
- Delete
- Query
  - Search by value
  - Get by index
  - Traverse

# SLL - Insert
<div class="columns">
    <img src="asset/image/singly_linked_list_insert_at_the_end.png">
    <img src="asset/image/singly_linked_list_insert_in_front.png">
</div>

# SLL - Search
<div class="columns">
    <img src="asset/image/singly_linked_list_search.png">
</div>
Time complexity O(n)

# SLL - Delete
<div class="columns">
    <img src="asset/image/singly_linked_list_delete_1.png">
    <img src="asset/image/singly_linked_list_delete_2.png">
</div>

- when we want to delete 7, how to do?
- when we want to delete 9, we can not just search 9, why?
- if we need delete the middle node, how to do
- if we need delete the first node, how to do?
- if we need delete the last node, how to do
- What is the time complexity Big-O?

# Implement Singly Linked List
[ch04_singly_linked_list.py](code/ch04_singly_linked_list.py)

# Design Doubly Linked Node
![bg right 10% w 80%](asset/image/doubly_linked_node_diagram.jpg)

# Implement Doubly Linked Node
[ch04_doubly_linked_node.py](code/ch04_doubly_linked_node.py)

# Doubly Linked List (DLL)
<div class="columns">
    <img src="asset/image/singly_linked_list_example.png">
    <img src="asset/image/doubly_linked_list_example.png">
</div>

- If we have two links in a single node of the list, we can reach any other node in the list, both before and after it.
- Weak points
  - Each node of a DLL takes up more space than SLL.
  - Each node insertion or deletion action, we need update two links.

# DLL - Insert
  <div class="columns">
      <img src="asset/image/double_linked_list_insert_at_front.png">
      <img src="asset/image/double_linked_list_insert_at_end.png">
      <img src="asset/image/double_linked_list_insert_in_middle.png">
  </div>

# Linked List Applications
[ch04_linked_list_applications](code/ch04_linked_list_applications.ipynb)