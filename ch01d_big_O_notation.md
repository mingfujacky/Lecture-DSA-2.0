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
    width: 60%;
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
# Big-O Notation
- A framework to measure algorithm performance 
- Measure terms
  - Time complexity
  - Memory space complexity
- Measure methods
  - Profiling (效能分析): implement algorithms and run code
  - Asymptotic analysis (漸近分析): find mathematical formulas that describe how an algorithm behaves as a function of its input

# Profiling 效能分析
```python
# implementation of an algorithm
def add_up_to(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

from time import process_time
input = [100_000, 1_000_000, 10_000_000, 100_000_000]

for n in input:
    start_time = process_time()
    add_up_to(n)
    end_time = process_time()
    elapsed_time = end_time - start_time
    print(f'{n=:>12,} took {elapsed_time:.3f} seconds')
```
**The performance is linear to input size n**

# Asymptotic Analysis 漸近分析
- Count operations of an algorithm
- Find a formula to express the number of operations as a function of input size n
- Classify the formula using Big-O notation
```python
def add_up_to(n):
    sum = 0                  # 1 op
    for i in range(1, n+1):  # n ops
        sum += i             # n ops 
    return sum               # 1 op
# total: (2n + 2) ops  ~~ O(n)
```
```python
def add_up_to(n):
    return (1 + n) * n / 2   # 1 op
# total:  1 op, regardless of the size of n  ~~ O(1)
```
# Count Operations
```python
for i in range(1, n+1):
    count += 1; sum += i             
```
$\sum_{i=1}^{n} 2$ = 2n ~~ O(n)

```python
for i in range(1, n+1):
    for j in range(1, n):
        count += 1; sum += i
```
$\sum_{i=1}^{n} \sum_{j=1}^{n-1} 2$ = $\sum_{i=1}^{n}2(n-1)$ = n*(2n-1) ~~ O(n²)

```python
for i in range(1, n+1):
    for j in range(i+1, n+1):
        result += 1         
```
$\sum_{i=1}^{n} \sum_{j=i+1}^{n} 1$ = $\sum_{i=1}^{n} (n-(i+1)+1)$ = $\sum_{i=1}^{n} (n-i)$ = n(n-1)/2 ~~ O(n²)

# 
- f(n) is a function of algorithm's running time, n is input size
- f(n)取 Big-O, 符號為O(g(n)), 當n夠大的時候, g(n)的常數倍是f(n)的上限
- 5n² + 6n + 9 = O(n²), because when n is large enough, 5n² + 6n + 9 <= C*n² (C is a constant)
- **f(n)=O(n²)**, means f(n) belongs to O(n²) class
![bg right:50% w:100%](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi4uqif112vvw150wphsw.jpg)

# Big-O Classify Growth Rate
- Big-O notation is to **<u>classify</u>** algorithm's performance (complexity) grow as the <u>input size n</u> grows.
<img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1657289969914/jdsAxrEyZ.JPG?auto=compress,format&format=webp" width="2000">
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)

# Four Rules to Find Big-O of an Algorithm
- Rule 1: Worst case
- Rule 2: Remove the constants
- Rule 3: Different inputs use different variables

```python
n = 9  # 1 op
m = 9  # 1 op
for i in range(n):         # Outer loop: n ops
    for j in range(m):     # Inner loop: m ops
        print(i, j)        # 1 op
# The summary of ops is n * (1 + (2 * m)) + 2. 
# The algorithm is  O(n + 2 * n * m + 2), n and m represent independent inputs. 
```
- Rule 4: Drop nondominant terms: We will get O(n * m)
**[Question]** Find Big O of an algorithm having time complexity 20n³ + 5n + 7 => O(n³)
https://dev.to/coderjay06/four-rules-for-big-o-1915

# The Big O of Linear Search
```python
def linear_search(self, target):
    for i in range(self._size):      # repeat n times
        if self._array[i] == target: # 1 op
            return i                 # 1 op
        elif self._array[i] > target:# 1 op
            return None              # 1 op
    return None                      # 1 op
```
- The formula for the running time of linear search is 
  T(n) = n * (1 + 2 ) + 1 = 3n +1 = O(n)

# The Big O of Binary Search
```python
def binary_search(self, target):
    left = 0                              # 1 op
    right = self._size - 1                # 1 op
    while left <= right:                  # repeat log2(n) times
        mid_index = (left + right) // 2     # 1 op
        mid_val = self._array[mid_index]    # 1 op
        if mid_val == target:               # 1 op
            return mid_index                # 1 op
        elif mid_val > target:              # 1 op
            right = mid_index - 1           # 1 op
        else
            left = mid_index + 1            # 1 op
    return None                             # 1 op
```
- The formula for the running time of binary search is
  T(n) = 2 + log<sub>2</sub>n*(6) + 1 = log<sub>2</sub>6n + 3 = O(log<sub>2</sub>n)

# Another 2 Notation of Algorithm Complexity
Case Type|Description|Notation
---------|-----------|--------
Worst Case|The maximum time the algorithm will take for any input. Analyzes the most unfavorable scenario. Usually the primary focus.|O(...)
Average Case|The expected time over all possible inputs. More complex to analyze, as it requires averaging over all input cases.|&Theta;(...)
Best Case|The minimum time the algorithm will take for any input. Represents the most favorable input scenario.|&Omega;(...)

# Complexity of Linear Search Algorithm
Case|Time Complexity
----|---------------
Best|&Omega;(1) (target is first item)
Avg|&Theta;(n)
Worst|O(n) (target is last or not found)

# Recap
- To evaluate performance of an algorithm, we can use asymptotic analysis, which means finding out a formula, expressed in big-O notation
- Big-O notation is used to classify functions based on their asymptotic growth. We use these classes of functions to express how fast the running time or memory used by an algorithm grows as the input becomes larger.
- Most common classes of functions
  – O(1): **constant**, sum up 1 to n
  – O(log<sub>2</sub>(n)): **logarithmic**, binary search
  – O(n): **linear**, linear search
  – O(n*log<sub>2</sub>(n)): **linearithmic**, priority queues
  – O(n<sup>2</sup>): **quadratic**, all pairs in an array.
  – O(2<sup>n</sup>): **exponential**, all subsets of an array

# Lab
The following table shows the running time (in seconds) of 4 programs given different size of input(n). Determine the Big-O notation for each program.(O(1), O(log10 n), O(n), O(n²), O(n³), O(2^n))
| n        | Program A | Program B | Program C | Program D |  
|----------|-----------|-----------|-----------|-----------|
| 10       | 1000      | 10        | 100       | 500       |
| 20       | 1001      | 40        | 200       | 650       |
| 100      | 1000      | 1000      | 1000      | 1000      |