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
# Binary Tree
Binary trees are defined by restricting each node to a maximum of two children.
- In a binary tree, a node may have zero, one, or two child links. 
- There are left children and right children of a node, and thus its left and right subtrees
 
<div class="middle-grid">
    <img src="asset/image/binary_tree_topology.png">
</div>

# Binary Tree Types
- Full Binary Tree: every node other than the leaves has two children.
- Perfect Binary Tree: all internal nodes have two children and all leaves are at the same level.
- Complete Binary Tree: all levels are completely filled except possibly the last level, and the last level has all keys as left as possible.
- Balanced Binary Tree: a binary tree in which the height of the two subtrees of any node never differ by more than one.
- Degenerate and Skewed Tree: each parent node has only one child. Such trees behave like linked lists.

# Binary Tree Illustration
![w:800 types of binary trees](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*cfgc3gvJ4cJiFB9G.png)

# Binary Tree Properties
- The max number of nodes at level 'l' of a binary tree is 2<sup>l</sup>, where root is at level 0.
- The max number of nodes in a binary tree of height 'h' is 2<sup>(h+1)</sup> - 1.
- In a binary tree, n<sub>0</sub> = n<sub>2</sub> + 1, where n<sub>0</sub> is the number of leaf nodes and n<sub>2</sub> is the number of nodes with two children.
- With 'n' nodes, the min possible height is ⌈log2(n + 1)⌉ − 1 under complete or perfect binary tree
- In a complete binary tree, given a node with an index i > 0, its parent’s index is (i - 1) // 2, and its children's indexes are (2 * i + 1) and (2 * i + 2)

# Design Binary Tree Node
![w:500 binary tree node diagram](asset/image/binary_tree_node_diagram.png)
[code/ch09_binary_tree_node.py](code/ch09_binary_tree_node.py)

# ADT - Binary Tree
![w:500 binary tree diagram](asset/image/binary_tree_diagram.png)
[code/ch09_binary_tree.py](code/ch09_binary_tree.py)

# Binary Tree Applications:
- **Huffman Coding Trees**: used in data compression algorithms.
- **Binary Search Trees (BST)**: used for efficient searching and sorting.
- **Heaps**: used in priority queues and heap sort algorithms.

[![Huffman Coding Trees](https://i.ytimg.com/vi/6K4aZiwq1Jk/hqdefault.jpg)](https://youtu.be/6K4aZiwq1Jk?si=rapnCX5zd5iqOW_a)

# Huffman Coding Tree Construction
- Given the following characters and their frequencies, construct a Huffman coding tree: A: 45, B: 13, C: 12, D: 16, E: 9, F: 5
- Steps to construct the tree:
  1. Create a leaf node for each character and build a min-heap of all leaf nodes.
  2. While there is more than one node in the heap:
     - Extract the two nodes of the lowest frequency from the heap.
     - Create a new internal node with these two nodes as children and with frequency equal to the sum of their frequencies.
     - Insert the new node back into the heap.
  3. The remaining node is the root of the Huffman tree.
- Huffman codes: A: 0, B: 101, C: 100, D: 111, E: 1101, F: 1100

# Huffman Coding Tree Visualization
[![Huffman Coding Trees](https://i.ytimg.com/vi/d3gHFesPc_E/hqdefault.jpg)](https://youtu.be/d3gHFesPc_E?si=HaMDpkypz_8Anv1A)

[code/ch09_huffman_coding_tree.py](code/ch09_huffman_coding_tree.py)
