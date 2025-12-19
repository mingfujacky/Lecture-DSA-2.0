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
# Python Code Hierarchy
![bg right:50% w:80% Module](https://www.beejok.com/tutorial_python_intermediate/img/packages_intro-01.jpg)

# Module
- Package: The top-level container. It is a folder that groups related modules together to help organize code and avoid naming conflicts.
- Module: A module is a **file** containing Python code that includes functions, variables, and other elements.
- Function: A function is a block of code that performs a specific task.
- Constant: Constants are variables whose values do not change during the program's execution.
- Other Elements: May contain classes, global variables, or import statements.

[Module material](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/L_module.ipynb)

# Package and Module
![bg right:70% w:100% Package and module](https://images.squarespace-cdn.com/content/v1/590eeff5b8a79b2147a783be/3a8a5a39-1cbb-43a5-82ad-f4c49da41daf/Picture+1.png?format=2500w)

remark: the root is project name

# Homework
DSA HW (A)