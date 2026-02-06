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

# Binary Search Trees
A binary search tree (BST) has some properties
- It’s a tree
- It’s binary, so each node has (optionally) a left and a right child
- It’s used for searching
- BST is potentially as fast as binary search on a sorted array.
- Insertion and deletion on BST can be faster than sorted arrays
- BST need more memory and more complicated than sorted array   

# BST is Order Matters
In BST, for any node N that stores a value v, all nodes in the left subtree of N will have values less than or equal to v, and all nodes in the right subtree of N will have values greater than v

<div class="middle-grid">
    <img src="asset/image/binary_tree_bst_order.png">
</div>

# Find the Minimum and Maximum Elements in a BST
- Get the maximum element, we start at the root and follow the links to the right children until we reach a node that has no right child. This node (which could be the root itself) stores the maximum value in the tree.
- Get the minimum element, we start at the root and follow the links to the left children until we reach a node that has no left child.
<div class="middle-grid">
    <img src="asset/image/binary_tree_bst_min_max.png">
</div>



# Implement BST's Node (2/2)
```python
```
# Implement BST Helper Functions
```python
class BinarySearchTree:
    def __init__(self):
        self._root = None
```

# Design BST Search
<div class="middle-grid">
    <img src="files/image/tree_search_1.png">
    <img src="files/image/tree_search_2.png">
</div>
The search method follows a single path, from the root to (possibly) a leaf, means that it will take no more steps than the height of the tree — it needs O(h) comparisons, where h is the height of the tree.

# Implement BST Search
```python
def _search(self, value):
    """Returns a tuple. 
       The first element is the node containing the target value, or None if not found.
       The second element is the parent of the node in the first position. 
       If the target wasn't found or if it was the root, the parent is set to None.
    """
    parent = None
    node = self._root
    while node is not None:
        node_val = node.value()
        if node_val == value:
            return node, parent
        elif value < node_val:
            parent = node
            node = node.left()
        else:
            parent = node
            node = node.right()
    return None, None
```

# Design BST Insert
<div class="middle-grid">
    <img src="files/image/tree_insert.png">
</div>

- In general, when we get to a node, we first check the value it stores to understand which branch we need to traverse and whether we need to go left or right. 
- Suppose we figure out that we need to go right. If the node has no right child, we have found the place where we have to add the new element. 
- All we have to do is create a new node and attach it as a right child of the current node. 

# Implement BST Insert
```python
def insert(self, value):       
        node = self._root
        if node is None: # Empty tree
            self._root = Node(value)
            return None
        
        while node is not None:
            if value <= node.value():
                if node.left() is ????:
                    node.set_????(Node(value))
                    break
                else:
                    node = node.????() # We keep traversing the left branch
            elif node.right() is ????:
                    node.set_?????(Node(value))
                    break
            else:
                node = node.?????()  # We keep traversing the right branch
```

# Design DST Delete (1/2)
 - Case 1: delete a leaf
 - Case 2: delete a node with only one child
 - Case 3: delete a node having two children

<div class="middle-grid">
    <img src="files/image/tree_delete_cases.png">
    <img src="files/image/tree_delete_leaf.png">
    <img src="files/image/tree_delete_one_child.png">
</div>

# Design DST Delete (2/2)
<div class="middle-grid">
    <img src="files/image/tree_delete_two_children_1.png">
    <img src="files/image/tree_delete_two_children_2.png">
    <img src="files/image/tree_delete_two_children_3.png">
</div>

# Implement BST Delete
```python
def delete(self, value):
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('Value not found')
        if node.left() is None or node.right() is None:  # The node has at most only one child
            if node.left() is None:
                maybe_child = node.right() 
            else:
                maybe_child = node.left()
            if parent is None:  # The node is the root
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else: # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None: # M is the left child of N.
                new_node = Node(max_node.value(), None, node.right())
            else:
                new_node = Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            # Then  replace the node to be deleted with a new node with M.value(), and the same subtrees as N.
            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)
```
# Illustrate BST Delete
<div class="middle-grid">
    <img src="files/image/tree_delete_example_1.png">
    <img src="files/image/tree_delete_example_2.png">
    <img src="files/image/tree_delete_example_3.png">
</div>

# Tree Category
<div class="columns">
    <img src="files/image/tree_category.png">
</div>

