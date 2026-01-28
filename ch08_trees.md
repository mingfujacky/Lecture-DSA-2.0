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
- A generic **tree** is a data structure that consists of nodes connected by links. 
- Each node contains a value and a variable number of links to other nodes, from zero to some number k (the branching number of a k-ary tree, that is, the maximum number of links a node can have).

# Terminology of Tree (1/2)
- Root: no other node in the tree points to the root (0)
- Parent and Child node: a node P has a link to another node C, then P is called the **parent** of C, and C is a **child** of P. 0 is the parent node of two child nodes: 2 and 8
- Leaf: a node has no links to children (5, 1, 2, 3, 4, 7)
- Internal node: node has child nodes (2, 8, 6, 3)
- No loop in a tree: any path from the root to a leaf, you never see the same node twice

# Terminology of Tree (2/2)
- Ancestor: node N is an ancestor of node M if N is in the path between the root and M. 
- Descendant: a descendant of a node N is either one of the children of N or the descendant of one of the children of N. Node 8 is an ancestor of node 7.
- Sibling: All children of the same node are siblings.
- Subtree: a portion of the tree containing a node R and all the descendants of R.
- Height: the length of the longest path from the root to a leaf
<div class="middle-grid">
    <img src="asset/image/tree_terminology.png">
</div>

# Supplementary
[Geeks for geeks](https://www.geeksforgeeks.org/dsa/introduction-to-tree-data-structure/)
[W3Schools](https://www.w3schools.com/dsa/dsa_theory_trees.php)