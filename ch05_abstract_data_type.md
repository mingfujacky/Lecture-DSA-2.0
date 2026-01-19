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
# Abstract Data Types
- **Abstract data type (ADT)** is a abstract model for data types, defined by its behavior from the point of view of data users specifically in terms of 
  - possible values
  - possible operations
  - behavior of operations 
- Data structures we learned before, array and linked node, which are concrete representations of data in memory, and are the point of view of an implementer, not a user.
- ADT example: a STACK has push/pop operations that follow a Last-In-First-Out rule, and can be concretely implemented using either a linked node or an array.

# Three-Level Hierarchy
- **Abstract data type**: a theoretical concept that describes at a high level how data can be organized and the operations that can be performed on the data.
- **Data structure**: how data is organized in memory and the internal representation details of the DS
- **Implementation**: choose a programming language and translate the DS into code.
![bg right:40% w:90%](asset/image/abstract_data_type.png)

# A simple ADT: Bag
#### Bag is a container containing a finite number of objects.
- Objects in a bag have no particular order.
- Objects in a bag may be duplicated.
- Objects in a bag may be different types.

![bg right:50% w:90%](asset/image/bag_diagram.png)


# Behaviors of Bag
- Adding/removing:
  – Add a given object to the bag.
  – Remove an occurrence of a specific object from the bag.
  – Remove all objects from the bag.
- Counting:
  – Get the number of items currently in the bag.
  – See whether the bag is empty.
  – Count the number of a specific item in the bag.
- Query:
  – Test whether the bag contains a particular object.
  – Look at all objects in the bag.

# Bag ADT Specification
A bag is a collection of objects with 2 methods:
- insert(x)— allow a client to add a single element to the bag. The order of insertion is not important.
- iterate() — allow a client to go through all the elements in the bag. The order in which elements are iterated is not guaranteed.
- Data structure : Singly Link
- Implementation: Python

# Implementation of Bag
```python
class Bag:
    def __init__(self):
        self._data = SinglyLinkedList()

    def insert(self, value):
        self._data.insert_in_front(value)

    def iterate(self):
        return self._data.traverse()        
```