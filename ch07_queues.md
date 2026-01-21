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
# Chapter 9: Queue
![bg right:50% w:90%](files/image/queue_ice_cream.png)
- **Queue** is a container that allows elements to be added or removed according to FIFO rule (first in, first out).

# Requirements of a Queue
Queue follows FIFO rule, we design its interface with only two methods:
- Enqueue(): insert an element into the queue
- Dequeue(): remove the least recently added element from the queue and return it

<div class="columns">
    <img src="files/image/queue_operations.png">
    <img src="files/image/queue_illustration.png">
</div>

# Consider Data Structures to Implement Queue
- Static array
- Dynamic array (complicated)
- Doubly linked list
- Stack (complicated)
<div class="middle-grid">
    <img src="files/image/queue_static_array.png">
    <img src="files/image/queue_static_array_full.png">
    <img src="files/image/queue_linked_list.png">
</div>

# Use Two Stacks to Implement Queue
![bg right:60% w:90%](https://hetalrachh.home.blog/wp-content/uploads/2020/04/queue-using-two-stacks.png)

# Design Queue by Static Array
When 'Rear' reaches the end of static array and there are some unused space at the front.
- Move all elements in the queue toward the start of the array. This means an O(n) overhead. It is inefficient.
- Circular queue

<div class="middle-grid">
    <img src="files/image/queue_circular_1.png">
    <img src="files/image/queue_circular_2.png">
    <img src="files/image/queue_circular_3.png">

</div>

# Comparison of Possible Implementations
Alt|Enqueue| Dequeue()| Dynamic size
---|---------|----------|-------------
Static array| O(1)| O(1)| No
Dynamic array| O(n)|O(n)|Yes
Doubly linked list | O(1)| O(1)| Yes

# Implement Queue by Doubly Linked List
```python
class Queue:
    def __init__(self):
        self._data = ????????????????()
    def __len__(self):
        return ???(self._data)
    def __str__(self):
        return str(self._data)
    def is_empty(self):
        return self._data.is_empty()
    def enqueue(self, value):
        self._data.??????????????(value)
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self._data.?????????????????()
```

# Implement Queue by Static Array - Init and Helper
```python
def __init__(self, max_size):
        # Creates a static array under list with max_size >= 2
        if max_size <= 1:
            raise ValueError(f'Invalid size (a queue must have at least two elements): {max_size}')
        self._data = [None] * ????????
        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._size = 0

def __str__(self):
        if self.is_empty():
            return 'empty queue'
        result = []
        front = self._front
        if front >= self._rear:
            while front ? self._max_size:
                result.append(self._data[front])
                front += 1
            front = ?
            while front ? self._rear:
                result.append(self._data[front])
                front += 1
        else:
            while front ? self._rear:
                result.append(self._data[front])
                front += 1        
        return f"Queue {' -> '.join(map(str, result))}"
```
# Implement Queue by Static Array - Check Size
```python
def __len__(self):
        return self.?????

def is_empty(self):
        return len(self) == ?

def is_full(self):
        return len(self) == self.?????????                
```

# Implement Queue by Static Array - Enqueue
<div class="middle-grid">
    <img src="files/image/queue_static_array_enqueue1.png">
    <img src="files/image/queue_static_array_enqueue2.png">
    <img src="files/image/queue_static_array_enqueue3.png">
</div>

```python
def enqueue(self, value):
        if self.is_full():
            raise ValueError('The queue is already full!')
        self._data[self._rear] = value
        self._rear = (self._rear ? 1) % self.?????????
        self._size += 1
```

# Implement Queue by Static Array - Dequeue
<div class="middle-grid">
    <img src="files/image/queue_static_array_dequeue1.png">
    <img src="files/image/queue_static_array_dequeue2.png">
    <img src="files/image/queue_static_array_dequeue3.png">
</div>

```python
def dequeue(self):
    if self.is_empty():
        raise ValueError("Cannot dequeue from an empty queue")
    value = self._data[self._front]
    self._front = (self._front ? 1) % self.?????????
    self._size -= 1
    return f"{value} dequeued from the queue"
```

# What about dynamic arrays?
- When we try to enqueue an element on a full queue, we can just allocate a new array with double size.
- If we copy the array as it is over the new array, we will encounter a big problem: the rear and front pointers will no longer make sense  
<div class="middle-grid">
    <img src="files/image/queue_dynamic_array_enqueue1.png">
    <img src="files/image/queue_dynamic_array_enqueue2.png">
</div>
This won’t be any slower than copying the elements in the same positions as they were, and it won’t affect the Big-O. But it will make the code more complicated.

# Recap
- A queue is a container that adheres to the FIFO policy
- Queues are widely used in computer science and programming, including messaging systems, networking, web servers, and operating systems
- Queues provide two operations: enqueue and dequeue
- A queue can be implemented using either arrays or doubly linked lists to store its
elements.
  - Using doubly linked lists, enqueue and dequeue take O(1) time in the worst case.
  - Using static arrays, we can implement a circular queue, where the array is imagined as a circular container.
  - Using dynamic arrays to implement queue is quite complicated and not very common.

# Backup
# Homework
DSA HW (H): Implement queue using stacks