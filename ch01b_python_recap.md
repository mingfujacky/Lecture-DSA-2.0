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
    color: lightskyblue;  
  }

  .small-text {
    font-size: 0.75rem;
  }
---
# Python Integrated Development Environment (IDE)
- **Thonny**
- Google Colab
- VSCode
- Jupyter Notebook

[Thonny installation and introduction](https://github.com/mingfujacky/Lecture-Python/blob/main/1_python_basic/C_thonny_introduction.md#一個可以執行-python-程式碼的環境)



# Python Standard Data Structures
![bg right:50% w:90% Python built-in data types](files/image/data_structure_category.jpg)
<div class="columns">
<div>

## Primitive
- [Data types](https://github.com/mingfujacky/Lecture-Python/blob/main/1_python_basic/D_data_type.ipynb)
- [String](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/A_string.ipynb)
- [Number: Int and Float](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/C_number.ipynb)
- [Bool](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/D_logic.ipynb)
</div>

<div>

## Container
- [Tuple](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/E_tuple.ipynb)
- [List](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/F_list.ipynb)
- [Set](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/G_set.ipynb)
- [Dict](https://github.com/mingfujacky/Lecture-Python/blob/main/2_python_middle/H_dictionary.ipynb)
</div>

</div>

# Python Syntax
- [Flow Control](https://github.com/mingfujacky/Lecture-Python/blob/main/1_python_basic/H_flow_control.ipynb)
- [Function](https://github.com/mingfujacky/Lecture-Python/blob/main/1_python_basic/I_function.ipynb)