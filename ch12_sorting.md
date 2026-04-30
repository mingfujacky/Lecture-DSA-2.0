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
# Sorting
- In computer science, sorting is the process of arranging data in a specific order (typically numerical or alphabetical).
- Sorting algorithms are fundamental for optimizing search operations, organizing data, and improving the efficiency of various applications.
  - Search efficiency: searching through a sorted list (e.g., using Binary Search) is significantly faster than an unsorted one.
  - Data visualization: it is easier to identify trends, minimums, and maximums when data is ordered.
  - Foundation for other algorithms: many complex algorithms (like Kruskal's for spanning trees) require sorted data as an input.

# Sorting Algorithm Terminology
- Stable: data with same value keeps same relative order after sorting as it had before.
- Unstable: data with same value might not keep its original relative order after sorting.
- Internal Sort: All sorting operations are completed entirely within RAM.
- External Sort: Used when the dataset is too large to fit in the main memory. The sorting process requires transferring data back and forth from external storage (like a HD).
- Time Complexity: the total amount of time an algorithm takes.
- Space Complexity: the total amount of memory space required to run the algorithm.
- In-place: The sorting is done directly within the original data structure (like the original array). It does not require extra memory space for temporary, auxiliary data structures.
- Out-place: Requires the use of temporary, auxiliary data structures to perform the sorting, thereby occupying extra memory space.

# Sorting Algorithms
- Basic sorting algorithms are often used for education to build concepts.
  - Bubble sort
  - Selection sort
  - Insertion sort
- Advanced sorting algorithms are more efficient for large datasets in real applications.
  - Merge sort
  - Quick sort
  - Heap sort
  - Radix sort

# Bubble Sort: The "Lightest Rises to the Top"
- It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- Logic: in each pass, the largest unsorted element "bubbles up" to its correct position at the end of the list.
- Efficiency: $O(n^2)$ — inefficient for large datasets but great for teaching logic.
[![Bubble Sort Algorithm](https://i.ytimg.com/vi/O21rlLWDmco/mqdefault.jpg)](https://youtu.be/O21rlLWDmco?si=wXPrk9x1ishOpg2a)
[ch12_sorting_bubble.py](code/ch12_sorting_bubble.py)

# Selection Sort: "Finding the Smallest"
- It divides the list into a "sorted" part and an "unsorted" part. It repeatedly finds the minimum element from the unsorted part and moves it to the beginning.
- Logic: search the whole unsorted list for the smallest item, swap it with the first unsorted item, and repeat.
- Efficiency: $O(n^2)$.
[![Selection Sort Algorithm](https://i.ytimg.com/vi/6W_ZdOzCcg8/mqdefault.jpg)](https://youtu.be/6W_ZdOzCcg8?si=oxLQKo8VBB_PaVeM)
[ch12_sorting_selection.py](code/ch12_sorting_selection.py)

# Insertion Sort: "The Card Player's Method"
- Most people sort a hand of playing cards. You take one item at a time and "insert" it into its correct position among the items you have already sorted.
- Logic: Build the sorted list one item at a time by shifting larger elements to the right.
- Efficiency: $O(n^2)$.
[![Insertion Sort Algorithm](https://i.ytimg.com/vi/9ufqiy4VlLI/mqdefault.jpg)](https://youtu.be/9ufqiy4VlLI?si=Nu88ifB48hL9dWCw)
[ch12_sorting_insertion.py](code/ch12_sorting_insertion.py)

# Summary Table of Basic Sorting Algorithm
| Algorithm | Best Case | Worst Case | Intuition |Stability |
|-----------|-----------|------------|-----------|----------|
| Bubble Sort | $O(n)$ | $O(n^2)$ | Swapping neighbors | Stable |
| Selection Sort | $O(n^2)$ | $O(n^2)$ | Finding the minimum | Unstable |
| Insertion Sort | $O(n)$ | $O(n^2)$ | Placing cards in a hand | Stable |

# Merge Sort: "The Divide and Conquer Strategy"
- Just as you might organize a large pile of documents by splitting them into two smaller stacks, sorting those, and then carefully merging them back together, Merge Sort uses a recursive approach to handle data.
- Logic: It continuously splits the list in half until each sub-list contains only one element (which is inherently sorted), then merges those sub-lists back together in the correct order.
- Efficiency: $O(n \log n)$. This is significantly faster than Insertion Sort for large datasets because it avoids the nested comparisons over the entire list.

# Key Steps of Merge Sort
- Divide: Find the midpoint of the list and split it into a left half and a right half.
- Conquer: Recursively apply the sort to both halves.
- Combine (Merge): Compare the smallest elements of each half and move the smaller one into a new array, repeating until all elements are merged back into a single sorted list.
[![Merge Sort Algorithm](https://i.ytimg.com/vi/m51fKDSU0PU/mqdefault.jpg)](https://youtu.be/m51fKDSU0PU?si=Vnqzp0rSCzOAepip)
[ch12_sorting_merge.py](code/ch12_sorting_merge.py)

# Quick Sort: "The Partitioning Strategy"
- Imagine you are organizing a group of people by height. You pick one person as a "pivot," then ask everyone shorter to stand on their left and everyone taller to stand on their right. You then repeat this process for the two smaller groups until everyone is in the correct order.
- Logic: selects a "pivot" element and partitions the array into two sub-arrays—those smaller than the pivot and those larger. It then recursively sorts the sub-arrays.
- Efficiency:Average Case: $O(n \log n)$.Worst Case: $O(n^2)$ (occurs when the pivot is consistently the smallest or largest element).

# Key Steps of Quick Sort
- Pick a Pivot: Choose an element from the array (common strategies include picking the first, last, or middle element).
- Partitioning: Rearrange the array so that all elements with values less than the pivot come before it, and all elements with values greater than the pivot come after it.
- Recursive Call: Apply the same logic to the sub-array of smaller elements and the sub-array of larger elements.

[![Quick Sort Algorithm](https://i.ytimg.com/vi/btNp7BRiUxE/mqdefault.jpg)](https://youtu.be/btNp7BRiUxE?si=mg7Hpz7QPjoZ2Az6)
[ch12_sorting_quick.py](code/ch12_sorting_quick.py)

# Heap Sort: "The Priority Queue Method"
- Imagine you are organizing a large group of people and you always want to pick the tallest person next. You arrange everyone into a "human pyramid" (a binary tree) where every person is taller than the two people standing below them. Once you take the person at the top, you quickly reorganize the pyramid to find the next tallest person.
- Logic: It converts the list into a Max-Heap (a complete binary tree where every parent is greater than its children). It then repeatedly removes the largest element from the heap and places it at the end of the list, "heapifying" the remaining elements to maintain the structure.
- Efficiency: O(nlogn) for all cases. It is an in-place sort, meaning it requires very little extra memory compared to Merge Sort.

# Key Steps of Heap Sort
- Build Max-Heap: transform the unsorted array into a heap structure where the largest value is at the root (index 0).
- Swap and Shrink: Swap the root element (maximum value) with the last element of the heap. Consider this last element as "sorted" and removed from the heap.
- Re-heapify: fix the heap property for the new root by "push down" the element until the remaining unsorted portion is a valid Max-Heap again.

[![Heap Sort Algorithm](https://i.ytimg.com/vi/2DmK_H7IdTo/mqdefault.jpg)](https://youtu.be/2DmK_H7IdTo?si=37jg7_L2R6sB-ljW)
[ch12_sorting_heap.py](code/ch12_sorting_heap.py)

# Radix Sort: "The Digit-by-Digit Organizer"
- Imagine sorting a stack of mail by ZIP code. Instead of comparing two full addresses at once, you first group them by the last digit, then the second-to-last, and so on until you reach the first digit. By the end, the entire stack is perfectly ordered.
- Logic: A non-comparative sorting algorithm that avoids direct element-to-element comparisons. It processes numbers digit by digit, typically from the Least Significant Digit (LSD) to the Most Significant Digit (MSD), using a stable sub-sort (like Counting Sort) as a bucket manager.
- Efficiency: $O(d \cdot (n + k))$, where $n$ is the number of elements, $k$ is the range of digits (usually 10 for decimal), and $d$ is the number of digits in the largest number.

# Key Steps of Radix Sort
- Find the Maximum: Identify the number with the most digits to determine how many passes are required.
- Bucket Distribution: starting from the ones place, place each number into a "bucket" (0–9) based on the current digit.
- Collect and Repeat: flatten the buckets back into the main list. Move to the tens place, hundreds place, etc., and repeat until all digit positions are processed.

[![Radix Sort Algorithm](https://i.ytimg.com/vi/Uey0-GOMtT8/mqdefault.jpg)](https://youtu.be/Uey0-GOMtT8?si=fufjl05piwGHWT94)
[ch12_sorting_radix.py](code/ch12_sorting_radix.py)

# Summary Table of Advanced Sorting Algorithms
| Algorithm | Best Case | Worst Case | Intuition |Stability |
|-----------|-----------|------------|-----------|-----------|
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | Divide and conquer | Stable |
| Quick Sort | $O(n \log n)$ | $O(n^2)$ | Partitioning around a pivot | Unstable |
| Heap Sort | $O(n \log n)$ | $O(n \log n)$ | Using a binary heap structure | Unstable |
| Radix Sort | $O(d \times (n + k))$ | $O(d \times (n + k))$ | Sorting digit by digit into buckets | Stable |

Note for Radix Sort: $d$ is the number of digits, $n$ is the number of elements, and $k$ is the base (e.g., 10).

# Recap
- Sorting is a fundamental operation in computer science that organizes data in a specific order.
- Basic sorting algorithms (Bubble, Selection, Insertion) are simple but inefficient for large datasets.
- Advanced sorting algorithms (Merge, Quick, Heap, Radix) are more efficient and suitable for larger datasets, each with its own unique approach and use cases.
- Understanding the strengths and weaknesses of each sorting algorithm is crucial for selecting the right one for a given problem.