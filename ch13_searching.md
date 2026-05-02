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
# Searching
- Searching is the process of finding the location of a target value within a collection of data. It is a fundamental operation in Computer Science, used in everything from database queries to finding a contact on your phone.
  - Input: a collection of elements and a target value.
  - Output: the index (position) of the target if found, or a signal (like -1) if the target does not exist in the collection.
- Searching algorithms are fundamental for optimizing search operations, organizing data, and improving the efficiency of various applications.

# Searching Algorithms 
- **Linear Search**: A simple algorithm that checks each element in the list sequentially until the desired element is found or the list ends.
- **Binary Search**: An efficient algorithm that works on sorted lists by repeatedly dividing the search interval in half until the target value is found or the interval is empty.
- **Interpolation Search**: An improvement over binary search for uniformly distributed data, which estimates the position of the target value based on the values at the ends of the search interval.
- **Hashing**: A technique that uses a hash function to map data to a fixed-size array, allowing for fast retrieval of values based on keys.

# Linear Search
- It is the most straightforward searching algorithm.
- Logic: checks every element in the list one by one until the match is found or the end of the list is reached.
- Best For: unsorted data or small datasets.
- Time Complexity:$O(n)$
[![Linear Search Algorithm](https://i.ytimg.com/vi/19hcyQN8J7o/mqdefault.jpg)](https://youtu.be/19hcyQN8J7o?si=6ZA8nYvBayKBWF6Z)
[ch13_searching_linear.py](code/ch13_searching_linear.py)

# Binary Search
- It is a much faster algorithm, but it carries a strict requirement: the data must be sorted.
- Logic: Instead of checking every item, binary search eliminates half of the remaining elements in every step.
- Best For: sorted data or large datasets.
- Time Complexity:$O(\log n)$
[![Binary Search Algorithm](https://i.ytimg.com/vi/s2VsK_UqO9E/mqdefault.jpg)](https://youtu.be/s2VsK_UqO9E?si=0kbYo4KY4N7lS8eW)
[ch13_searching_binary.py](code/ch13_searching_binary.py)

# Interpolation Search
- It is an improvement over binary search for uniformly distributed data.
- Logic: It estimates the position of the target value based on the values at the ends of the search interval.
- Best For: uniformly distributed sorted data.
- Time Complexity: Average case is $O(\log \log n)$, but worst case can degrade to $O(n)$ if the data is not uniformly distributed.
[![Interpolation Search Algorithm](https://i.ytimg.com/vi/DlCPTPQD6Mw/mqdefault.jpg)](https://youtu.be/DlCPTPQD6Mw?si=nVAv2vktgQ1mnEKA)
# Interpolation Search (Cont.)
$$pos = low + \left[ \frac{(target - arr[low]) \times (high - low)}{arr[high] - arr[low]} \right]$$
$low$: The starting index of the current range.
$high$: The ending index of the current range.
$target$: The value we are searching for.
$arr[low]$: The value at the start of the range.
$arr[high]$: The value at the end of the range.
[ch13_searching_interpolation.py](code/ch13_searching_interpolation.py)

# Comparison of Searching Algorithms
For a dataset of $n = 4,294,967,296$ ($2^{32}$ elements):

|Algorithm|Complexity|Max Steps (Calculated)|
|---------|----------|-----------------------|
|Linear Search|O(n)|~4.2 Billion steps|
|Binary Search|O(logn)|32 steps|
|Interpolation Search|O(log(logn))|~5 steps|

# Hashing
- In previous searching topics, searching for a specific item often requires checking or comparing every element one by one $O(n)$ or using Binary Search $O(\log n)$.
- Hashing aims to achieve Instant Access $O(1)$ by using a mathematical trick, **hash function**, instead of searching for a value, we use the value itself to calculate exactly where it is stored.

# Hash Function
- A Hash Function is a mathematical algorithm that transforms an input (often a large or variable-sized "key") into a fixed-size numerical value (the "hash code" or "index"). In Computer Science, this value tells us exactly where to store or find data in a Hash Table. *"Fixed-size" refers to the Index range (e.g., 0–99) to fit an array.*
- Hash function takes an input (key) and converts it into a specific index in an array (a bucket). <span class="blue-text">*f(key)* $\rightarrow$ index</span>
  - Input (Key): can be a string "Alice", an integer 1024, or even a file.
  - The Function: a consistent formula, like $index = key \bmod size$.
  - Output (Index / Hash Value / Hash Code): A fixed integer used as an index for an array.


# Hash Table
> A Hash Table is a data structure that uses a hash function to map keys to indices in an array, allowing for fast data retrieval. It is designed to provide efficient insertion, deletion, and lookup operations.





| Hash Table | Hash Concept |
| :---: | :---: |
| ![Hash Table w:400](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1920px-Hash_table_3_1_1_0_1_0_0_SP.svg.png) | [![Illustration of Hashing](https://i.ytimg.com/vi/-ESq4cqwW7I/mqdefault.jpg)](https://youtu.be/-ESq4cqwW7I?si=nvugn6k47i0ej2bX&t=161)



# Properties of a Good Hash Function
- Deterministic: The same input must always produce the exact same output. If "Apple" results in index 5 today, it must result in index 5 tomorrow.
- Efficient: It must be very fast to calculate ($O(1)$). If the function takes too long, we lose the speed benefit of hashing.
- Uniform Distribution: It should spread keys out evenly across the table. We want to avoid collisions where many keys end up at the same index.

# Hash Functions - Division Modulo Method
  >$hash(key) = key \bmod{table\_size}$

Suppose we have a hash table with 10 slots ($m=10$).

- If key is 24: $24 \bmod{10} = 4$ (Store at index 4)
- If key is 50: $50 \bmod{10} = 0$ (Store at index 0)
- If key is 137: $137 \bmod{10} = 7$ (Store at index 7)

# Hash Functions - Multiplication Method
>$hash(key) = \lfloor table\_size \times (key \times A \mod 1) \rfloor$ ,$A$ is a constant (0 < A < 1).

Key is 123 and 124, small table ($m=100$), constant A = 0.618
| Key = 123 | Key = 124 |
| :---: | :---: |
|123 * 0.618 = 76.014 | 124 * 0.618 = 76.632
|Fractional part: 0.014 | Fractional part: 0.632
|Scale by m: 100 * 0.014 = 1.4 | Scale by m: 100 * 0.632 = 63.2
| Floor: $\lfloor 1.4 \rfloor = \mathbf{1}$ | Floor: $\lfloor 63.2 \rfloor = \mathbf{63}$
| Index 1 | Index 63 |

# Hash Function - Mid-Square Method
>$hash(key) = \text{Extract middle digits of } (key^2)$

Key: $k = 45$
Square: $45^2 = 2025$
Hash Value: If we need a 2-digit index, we take the middle digits "02".

# Hash Functions - Folding Method
>$hash(key) = \text{Sum of parts of the key}$

Key = 123456789 and Table Size = 1000
Step 1: Split into 123, 456, 789.
Step 2: $123 + 456 + 789 = 1368$.  
Step 3: $1368 \bmod{1000} = 368$.


# Hash Functions - Digit Analysis Method
>$hash(key) = \text{Extract specific digits from the key}$

The Digit Analysis Method is a technique where you select specific digits from the key and rearrange them to form the hash index. This method relies on analyzing the distribution of digits in the entire set of keys to avoid collisions.

Imagine a company where IDs are 8 digits long. After looking at a list of 500 employees, you notice the following pattern:

Digits 1–2 (Year of Hire): Most start with 24, 25, or 26.

Digits 3–4 (Department Code): 10 for Sales, 20 for Engineering, 30 for HR.

Digits 5–8 (Unique Sequence Number): A randomly assigned sequence from 0001 to 9999.

# Hash Functions - Digit Analysis Method(Cont.)
We might form a 2-digit index by extracting the 5th and 7th digits.
|Employee ID|Digit 5|Digit 7|Hash Index|
|---|---|---|---|
|26104521|4|2|42|
|26208214|8|1|81|
|25101977|1|7|17|
|24306308|6|0|60|

# Cryptographic Hash Functions
- In a standard Data Structures course, we use hashing for searching speed. However, in Security and Cryptography, we use hashing for trust and integrity.
- Cryptographic Hash Function is a "one-way" mathematical algorithm that takes any amount of data and turns it into a unique, fixed-length string of characters(fingerprint).
- Popular Cryptographic Hash Functions: SHA-256, MD5, SHA-1.

# The Challenge: Collisions
Since a Hash Table has a limited size, two different keys might calculate to the same index. This is called a Collision. Like we use $key \bmod{10}$, both 42 and 52 want to go to index 2
**Common Solutions:**
- Open Hashing - (Separate) **Chaining**: Each slot in the array points to a linked list. Multiple items at the same index are simply "chained" together.
- Closed Hashing - **Open Addressing** : If a slot is taken, the system looks for the next available empty slot based on a rule (e.g., just move to the next index).
  - Linear Probing: Check the next slot sequentially until an empty slot is found.
  - Quadratic Probing: Check slots at intervals that grow quadratically (1, 4, 9, etc.).
  - Double Hashing: Use a second hash function to determine the step size for probing.

# Collision Resolution - Chaining
- In Chaining, each index of the hash table contains a pointer to a linked list (or another data structure) that holds all the elements that hash to the same index. When a collision occurs, the new key-value pair is added to the linked list at that index.

![Chaining w:700](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*HuwomBMWpSH5qJTX.png)
[ch13_hashing_chaining.py](code/ch13_hashing_chaining.py)

# Collision Resolution - Open Addressing

| Linear Probing | Quadratic Probing | Double Hashing |
| :---: | :---: | :---: |
| ![Open Addressing Linear Probing:500](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2015/08/openAddressing1.png) | [![Illustration of Hashing](https://i.ytimg.com/vi/-Rdatfn7VUw/mqdefault.jpg)](https://youtu.be/-Rdatfn7VUw?si=1QCH8-tiPnzqaLk4) | [![Double Hashing](https://i.ytimg.com/vi/8nfPgBS43Dw/mqdefault.jpg)](https://youtu.be/8nfPgBS43Dw?si=SZbeZmwUSw7n4C1M) |
[ch13_hashing_linear_probing.py](code/ch13_hashing_linear_probing.py)

# Why Not Hashing for Everything?
Hashing is powerful, but it’s not a one-size-fits-all solution. It has its own set of challenges and limitations:
- Collisions: Even with a good hash function, collisions can still occur, which can degrade performance.
- Memory usage: Hash tables can consume more memory than other data structures, especially if the table is sparsely populated.
- Not ordered: Hash tables do not maintain any order of the keys, which can be a problem if you need to iterate through the data in a specific order and can not support range query, max/min query.
- Not suitable for all data field (like sex, school): Some data field may not have good hash functions, leading to poor performance.

# Recap
- Searching is a fundamental operation in Computer Science, and there are various algorithms designed to optimize this process.
- Linear Search is simple but inefficient for large datasets, while Binary Search is much faster but requires sorted data. Interpolation Search can be even faster for uniformly distributed data.
- Hashing is a powerful technique that allows for constant time complexity $O(1)$ for search operations, but it comes with its own challenges, such as collisions and memory usage.
- Choosing the right searching algorithm or data structure depends on the specific use case, the size of the dataset, and the requirements for speed and memory efficiency.
