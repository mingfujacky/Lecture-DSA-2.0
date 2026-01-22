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

# Stack Application - Infix to Postfix Conversion
因爲 infix 的計算較複雜，電腦會先將infix轉成postfix再算, infix轉換成postfix的方法如下
1. 由左而右讀infix，一次讀取一個token: [operator + - * / ()] 或 [operand 1 2 x y]
2. 如果是operand，直接輸出
3. 如果是operator，則必須根據operator stack的規則決定 push 或 pop
4. 所有token讀完後，如果 operator stack 不是空的，則將 operator 依序 pop 出來
5. operator stack rule
  - A：'(' 一律 push
  - B: ')' 需重複 pop operator stack中的operator，直到遇見')'一同抵銷
  - C: operator在stack中只能優先序大的壓小的。如果外面的operator優先序較大，則 push。否則（小於等於）就一直做 pop，直到遇見優先序較小的運算子或堆疊為空，再把外面的運算子 push 到 operation stack 中。

# Illustration of Infix to Postfix Conversion
> (A + B) * C - D / E ==> A B + C * D E / -
>  5 + 3 * 2 ==> 5 3 2 * +
> A + (B * (C - D) / E) ==> A B C D - * E / +

<style scoped>
table {
  font-size: 12px;
}
</style>
| Step | Token | Action             | Stack (Bottom → Top)| Postfix|
|------|-------|--------------------|---------------------|--------|
|1     |  (    | push               | (                   |        |
|2     |  A    | output             | (                   | A      |
|3     |  +    | push               | ( +                 | A      |
|4     |  B    | output             | ( +                 | A B    |
|5     |  )    | pop until (        |                     | A B +  |
|6     |  *    | push               | *                   | A B +  |
|7     |  C    | output             | *                   | A B + C|
|8     |  -    | pop *, then push - | -                   | A B + C *|
|9     |  D    | output             | -                   | A B + C * D|
|10    |  /    | push               | - /                 | A B + C * D|
|11    |  E    | output             | - /                 | A B + C * D E|
|12    | End   | pop all            |                     | A B + C * D E / -|

# Stack Application
[code/ch06_stack_applications.ipynb](code/ch06_stack_applications.ipynb)

# Recap
- A stack is a ADT that abides by the LIFO policy.
- Stacks provide two operations: push and pop. No other way to insert or delete elements, and search is generally not allowed.
- A stack can be implemented using either arrays or linked lists to store its elements.