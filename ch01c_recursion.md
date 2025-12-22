---
marp: true
theme: default
class: 
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
    color: blue;  
  }

  .small-text {
    font-size: 0.75rem;
  }
---
# Function
All programming languages implement four features in their functions:
- Functions have code that is run when the function is called.
- Arguments (that is, values) are passed to the function when it’s called. This is the input to the function, and functions can have zero or more arguments.
- Functions return a return value. This is the output of the function, though some programming languages allow functions not to return anything or to return null values like undefined or None.
- The program **remembers** which line of code called the function and **returns** to it when the function finishes its execution.

# Function Call (1)
```python
def a():
    print('a() was called.')
    b()
    print('a() is returning.')

def b():
    print('b() was called.')
    c()
    print('b() is returning.')

def c():
    print('c() was called.')
    print('c() is returning.')

a()
```

# Function Call (2) 
```python
def a():
    spam = 'Ant'
    print('spam is ' + spam)
    b()
    print('spam is ' + spam)
def b():
    spam = 'Bobcat'
    print('spam is ' + spam)
    c()
    print('spam is ' + spam)
def c():
    spam = 'Coyote'
    print('spam is ' + spam)
a()
```
# Call Stack
Call stacks remember where the execution returns at the end of a function call, and they also keep track of local variables and parameters for each function call.
![](/files/image/recursion_call_stack.png)

# Recursive Function
- A recursive function is a function that calls itself in order to solve a problem.
- Recursive functions consist of two main parts: the base case and the recursive case.
- The base case is a condition that stops the recursion, preventing infinite loops.
- The recursive case is where the function calls itself with a modified argument, gradually approaching the base case.
- A recursive function that calculates the factorial of a number: N! = N × (N - 1)!
```python
def factorial(n):
    if n == 0:
        #BASE CASE
        return 1
    else:
        #RECURSIVE CASE
        return n * factorial(n - 1)
```
Recursive functions typically follow this pattern:
- There are one or more base cases that are directly solvable without the need for further recursion.
- Each recursive call moves the solution progressively closer to a base case.

# Stack Overflow
- A stack overflow occurs when there is no base case or the base case is never reached, causing the function to call itself indefinitely.
- This leads to excessive memory usage as each function call is added to the call stack until it exceeds the maximum stack size allowed by the programming environment.
- Example of a recursive function that causes a stack overflow:
```python
def countDownAndUp(number):
    print(number)
    countDownAndUp(number - 1)
countDownAndUp(3)
```
```python
import sys
print(sys.getrecursionlimit())
```

# Base Cases and Recursive Cases
- Base Case: the recursion stops and provides a direct answer without further recursion.
- Recursive Case: call itself with modified arguments, moving closer to the base case.
- Example of a recursive function with both base and recursive cases:
```python
def countDownAndUp(number):
    print(number)
    if number == 0:
        # BASE CASE
        print('Reached the base case.')
        return
    else:
        # RECURSIVE CASE
        countDownAndUp(number - 1)
        print(number, 'returning')
        return
countDownAndUp(3)
```
# Visualizing Recursion with Call Stack
![w:500](/files/image/recursion_count_down_and_up.png)
- The call stack is handled by the program implicitly, so there is no call stack variable. Calling a function pushes a frame object to the call stack, and returning from a function pops a frame object from the call stack.

# Iteration vs. Recursion
- Whenever you find yourself asking, “Wouldn’t using a loop be easier?” the answer is almost certainly “Yes,” and you should avoid the recursive solution. 
- Recursion can be tricky for both beginner and experienced programmers, and recursive code isn’t automatically “better” or “more elegant” than iterative code. 
- However, on some occasions an algorithm cleanly maps to a recursive approach. Algorithms that involve tree-like data structures and require backtracking are especially suited for recursion. 

# Calculating Factorials
```python
# iterative algorithm
def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product
print(factorial(5))
```
```python
# recursive algorithm is not good when number is large, may cause stack overflow
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(5))
```
# Calculating Fibonacci Numbers
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
```python
# iterative algorithm
def fibonacci(n):
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a + b
    return a
print(fibonacci(10))
```
```python
# recursive algorithm is not good for performance, repeatedly calculating the same Fibonacci numbers
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))  
```

# Use Case of Recursion
- You never need to use recursion. No programming problem requires recursion.
- Use recursion when your problem has these characteristics:
  - involves a tree-like structure.
  - involves backtracking.
  - isn’t so deeply recursive as to potentially cause a stack overflow.
- A tree has a self-similar structure: the branching points look similar to
the root of a smaller subtree. 
- Recursion often deals with self-similarity and problems that can be divided into smaller, similar subproblems. 

# Summary
- A recursive function is a function that calls itself to solve a problem.
- Recursive functions consist of two main parts: the base case and the recursive case.
- Recursive functions have recursive cases, those in which a recursive call is made, and base cases, those where the function simply returns. If there is no base case or a bug prevents a base case from being run, the execution causes a stack overflow that crashes the program.
- Recursion is a useful technique, but recursion doesn’t automatically make code “better” or more “elegant.” 
- Sometimes an iterative solution is more efficient and easier to understand.