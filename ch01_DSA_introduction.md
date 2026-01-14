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
    gap: 0.5rem;
    align-items: start;
  }
  .middle-grid img {
    width: 75%;
    justify-self: start;
    display: block;
  }
  .middle-grid p, 
  .middle-grid ul,
  .middle-grid ol {
  margin: 0;
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
# Roadmap of Python Programmer
<div class="middle-grid">

<div>
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb_CZf_pQ9Zkg3ExzYj-WrOL8XFsCV8U7Dh0r5wDPWJrUdVGdhwNWZvx6_Mh2vh9Kxd1iyAV5jbcbXh67McVHuCl-FBe8-tv30ZYXBrksuKi6_dlwbjhUzfTVmEk6RmwsEjq_hJiBv1K4/s1600/S__5816325.jpg" width="100%"/>
</div>

<div>

> 核心: 輸入、處理、輸出的基本框架

> 結構: OOP讓程式有邏輯、易擴展

> 效率: DSA是程式運行的引擎

> 未來: 有了邏輯基礎，再來學習AI/ML

</div>

</div>

# Welcome to DSA
Data structures and algorithms (DSA) are the foundational tools of computer science. They allow us to write code that is not just correct, but also efficient.

* <span class="blue-text">**Data structures**</span> are specific ways of organizing and storing data so it can be accessed and modified effectively.
* <span class="blue-text">**Algorithms**</span> are the step-by-step procedures or "recipes" for performing calculations, data processing, and automated reasoning.
* Together, they help us balance the trade-offs between execution speed (<span class="blue-text">**Time Complexity**</span>) and memory usage (Space Complexity).

# Major Areas of DSA
- **The Containers (Data Structures)**
We can examine how we store data, starting with the differences between linear structures like Arrays and Linked Lists, or more complex ones like Trees and Graphs.
- **The Processes (Algorithms)**
We can look at the logic behind manipulating data, such as how we find a specific item (Searching) or arrange items in order (Sorting).
- **The Scorecard (Big O Notation)**
We can discuss how we measure the "cost" of our code to predict how its performance changes as the amount of input data grows.

# 5 Steps to Learn DSA
[![5 Steps to Learn DSA - Complete Roadmap To Learn DSA
](https://i.ytimg.com/vi/9KeE_uDsOI8/mqdefault.jpg)](https://youtube.com/shorts/9KeE_uDsOI8?si=1pKkHL-lAU4MXcAd)

1. Learn at least one programming language
2. Learn about complexity
3. Learn data structures and algorithms
4. Practice data structures and algorithms
5. Participate in programming challenges to test your skill and efficiency

# Categorize Data Structures (1/2)

<div class="grid">

<div>

![w:100% categories data structure](asset/image/categorize_data_structures_2.png)

</div>

<div>

<span class="small-text">

> **Built-in / ADT**: 實作層級分類 
   - Built-in：Python 已提供的內建資料型別
   - ADT：開發者需自行實作的抽象資料型別
> **Linear / Non-linear**: 邏輯結構分類
   - Linear：資料元素間有線性關係
   - Non-linear：資料元素間無線性關係

</span>

</div>

</div>

# Categorize Data Structures (2/2)
![w:900 categories data structure](asset/image/categorize_data_structures_1.png)

# Why Should I Care About Data Structure
### Solve Lottery by SET or LIST, which data structure is better?
[Code of Lottery](code/lottery_comparison.py)

# Time Complexity of Set Implementation
```python
def lottery_by_set(numbers):
    buyer_nums = set(numbers)
    # 產生開獎號碼
    lottery_nums = set()
    while len(lottery_nums) < 6:
        lottery_nums.add(random.randint(1, 49))

    bingo_nums = lottery_nums & buyer_nums  # 計算中獎號碼
    return lottery_nums, bingo_nums
```
- 產生開獎號碼: O(n) 隨著號碼增加，時間線性增加
- 計算中獎號碼: O(1) 集合運算，時間不隨號碼增加而增加

# Time Complexity of List Implementation
```python
def lottery_by_list(numbers):
    buyer_nums = list(numbers)   
    lottery_nums = [] # 產生開獎號碼
    while len(lottery_nums) < 6:
        num = random.randint(1, 49)
        if num not in lottery_nums:
            lottery_nums.append(num)
    bingo_nums = []              # 計算中獎號碼
    for num1 in lottery_nums:
        for num2 in buyer_nums:
            if num1 == num2:
                bingo_nums.append(num1)
                break
    return lottery_nums, bingo_nums
```
- 產生開獎號碼: O(n) 隨著號碼增加，時間線性增加
- 計算中獎號碼: O(n**2) 隨著號碼增加，時間成兩次方增加

# Brief Data Structures Types
[Types of Data Structures（Facebook 影片）](https://www.facebook.com/share/r/1B3QMzoAYA/?mibextid=wwXIfr)

# 與資料結構最常見對應的演算法
![w:900 categories data structure](asset/image/algorithms_by_data_structure.png)

# 演算法設計範式
![w:900 categories data structure](asset/image/algorithms_by_設計範式.png)

# Why Should I Care About Algorithms
### Searching a number by linear search vs binary search, which algorithm is better?
[Code of Search](code/lottery.py)

# Time Complexity of Linear Search
```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```
搜尋的時間複雜度: O(n) 隨著資料量增加，時間線性增加

# Time Complexity of Binary Search
```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

```
搜尋的時間複雜度: O(log n) 隨著資料量增加，時間對數增加


# A Mental Model for Applying Data Structures
![bg right:50% w:80% apply data structure](asset/image/a_mental_model_for_applying_data_structures.png)