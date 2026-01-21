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
# Stacks
![bg right:50% w:90%](asset/image/stack_in_stock_management.png)
- **Stack** is a container that allows elements to be added or removed according to LIFO rule (last in, first out).
- Example: stack of plates, browser history, undo mechanism in text editors, call stack in programming languages, etc.

# ADT: Stack
Stack follows LIFO rule, we design its interface with only two methods:
- Push(): insert an element into the stack
- Pop() or Top(): remove the most recently added element from the stack and return it
- We also need to keep track of the last element that was added to the stack, is called the **top** of the stack. 
<div class="columns">
    <img src="asset/image/stack_diagram.png">
    <img src="asset/image/stack_illustration.png">
</div>

# Consider Two Data Structures to Implement Stack
- Referential array: Python list
- Linked list: singly linked list (SLL)
<div class="middle-grid">
    <img src="asset/image/stack_referential_array.png">
    <img src="asset/image/stack_linked_list.png">
</div>

# Design by SLL
<div class="columns">
    <img src="asset/image/stack_push.png">
    <img src="asset/image/stack_pop.png">
</div>

# Implement by SLL
[code/ch06_stack_sll.py](code/ch06_stack_sll.py)

# Theory vs. the Real World
- Considering Big O
  - Stack by SLL: O(1)
  - Stack by Dynamic array: O(n), but if a large number of operations is performed, their amortized (攤銷的) cost can be considered O(1).
- Considering implementation
  - You shouldn’t implement your own library unless it’s absolutely necessary
  - If the library is critical for your application and can become a bottleneck, you should profile it.
  - You shouldn’t profile all your code though. Focus on the critical sections where optimization will improve efficiency the most.

# Profiling Example
- Class Stack in stack.py coded by SLL
- Class StackArray in stack_dynamic_array.py coded by List to simulate dynamic array

<div class="columns">
    <img src="files/image/stack_profiling_1.png">
    <img src="files/image/stack_profiling_2.png">
</div>

- Python provides an optimized, extremely efficient implementation for list. This
code is usually written in C and compiled for use in Python
- With linked lists, we must allocate a new node on each call to push and then
destroy a Node object on each pop. Allocating the memory and creating the
objects takes time.

# Stack Application - Evaluating Expression
- Infix notation: 3 + 2
- Postfix notation: 3 2 +
- In infix notation, 3 + 2 * 4 == 3 + (2 * 4) based on operator precedence, if we want to add 3 and 2 first, the formula will be (3 + 2) * 4
- In postfix notation, we use 3 2 4 * + and 3 2 + 4 * respectively
- 
<div class="columns">
    <img src="files/image/stack_postfix_1.png">
    <img src="files/image/stack_postfix_2.png">
</div>

# Recap
- A stack is a container that abides by the LIFO policy.
- Stacks provide two operations: push and pop. No other way to insert or delete elements, and search is generally not allowed.
- A stack can be implemented using either arrays or linked lists to store its elements.
  - Using dynamic arrays, push and pop take O(n) time in the worst case, but O(1) amortized time (over a large number of operations).
  - Using SLLs, push and pop take O(1) time in the worst case.
- The amortized performance of the two implementations is close, and profiling can help you understand which of the two implementations is more efficient in a
given programming language.

# Backup
# Homework
DSA HW (G)