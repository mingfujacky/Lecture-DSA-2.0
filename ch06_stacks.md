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
    grid-template-columns: repeat(4, minmax(0, 1fr));
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

# Design Stack Upon Array and SLL
- Array: referential array - Python list
- Linked list: singly linked list (SLL)
<div class="middle-grid">
    <img src="asset/image/stack_referential_array.png">
    <img src="asset/image/stack_linked_list.png">
    <img src="asset/image/stack_push.png">
    <img src="asset/image/stack_pop.png">
</div>

# Implement by List
[code/ch06_stack_list.py](code/ch06_stack_list.py)

# Implement by SLL
[code/ch06_stack_sll.py](code/ch06_stack_sll.py)

# Stack Application - Evaluating Expression
- Infix notation: 3 + 2
- Postfix notation: 3 2 +
- In infix notation, 3 + 2 * 4 == 3 + (2 * 4) based on operator precedence, if we want to add 3 and 2 first, the formula will be (3 + 2) * 4
- In postfix notation, we use 3 2 4 * + and 3 2 + 4 * respectively

<div class="columns">
    <img src="asset/image/stack_postfix_1.png">
    <img src="asset/image/stack_postfix_2.png">
</div>

# Stack Application
[code/ch06_stack_applications.ipynb](code/ch06_stack_applications.ipynb)


# Recap
- A stack is a ADT that abides by the LIFO policy.
- Stacks provide two operations: push and pop. No other way to insert or delete elements, and search is generally not allowed.
- A stack can be implemented using either arrays or linked lists to store its elements.