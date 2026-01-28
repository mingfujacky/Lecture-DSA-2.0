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
# Trees
![bg right:50% w:90%](asset/image/tree_concept.png)
- A generic **tree** is a non-linear data structure that consists of nodes connected by links. 
- Each node contains a value and a number of links to other nodes, from zero to some number k (k-ary tree)

# Terminology of Tree (1/3)
- Root: no other node in the tree points to the root (0)
- Parent and Child node: a node P has a link to another node C, then P is called the **parent** of C, and C is a **child** of P. 0 is the parent node of two child nodes: 2 and 8
- Leaf: a node has no links to children (5, 1, 2, 3, 4, 7)
- Internal node: node has child nodes (2, 8, 6, 3)
- No loop in a tree: any path from the root to a leaf, you never see the same node twice

# Terminology of Tree (2/3)
- Ancestor: node N is an ancestor of node M if N is in the path between the root and M. 
- Descendant: a descendant of a node N is either one of the children of N or the descendant of one of the children of N. Node 8 is an ancestor of node 7.
- Sibling: All children of the same node are siblings.
- Subtree: a portion of the tree containing a node R and all the descendants of R.
- Height: the length of the longest path from the root to a leaf
<div class="middle-grid">
    <img src="asset/image/tree_terminology.png">
</div>

# Terminology of Tree (3/3)
- Level of a node: the number of connections between the node and the root. Root is at level 0.
- Depth of a node: the length of the path from the root to the node. Root has depth 0.
- Degree of a node: the number of children of the node.
- Degree of a tree: the maximum degree of all nodes in the tree.
- Height of a node: the maximum number of edges between the node and a leaf node.
- Height of tree: the maximum number of edges from the root node to a leaf node. A tree with only one node (the root) has height 0.

# Supplementary Resources
[Geeks for geeks](https://www.geeksforgeeks.org/dsa/introduction-to-tree-data-structure/)
[W3Schools](https://www.w3schools.com/dsa/dsa_theory_trees.php)

# Compare Linked List to Trees
![](asset/image/tree_compart_linked_list.png)