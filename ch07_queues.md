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
# Queues
![bg right:50% w:90%](asset/image/queue_ice_cream.png)
- **Queue** is a container that allows elements to be added or removed according to FIFO rule (first in, first out).

# ADT: Queue
Queue follows FIFO rule, we design its interface with only two methods:
- Enqueue(): insert an element into the queue
- Dequeue(): remove the least recently added element from the queue and return it

<div class="columns">
    <img src="asset/image/queue_diagram.png">
    <img src="asset/image/queue_illustration.png">
</div>

# Design Queue Upon Array and SLL
- Array: referential array - Python list
- Linked list: singly linked list (SLL)
<div class="middle-grid">
    <img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1656974512885/7oqfru36G.jpg">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20250325130840080788/Queue-Linked-List-Implementation_.webp">
</div>

# Implement by List
[code/ch07_queue_list.py](code/ch07_queue_list.py)

# Implement by SLL
[code/ch07_queue_sll.py](code/ch07_queue_sll.py)
    
# (LeetCode 232) Implement Queue using Stacks
![bg right:60% w:90%](https://hetalrachh.home.blog/wp-content/uploads/2020/04/queue-using-two-stacks.png)

# Recap
- A queue is a container that adheres to the FIFO policy
- Queues are widely used in computer science and programming, including messaging systems, networking, web servers, and operating systems
- Queues provide two operations: enqueue and dequeue
