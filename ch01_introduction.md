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
# Roadmap of Python Programmer
![Newbie programmer bg right:35% w:90%](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb_CZf_pQ9Zkg3ExzYj-WrOL8XFsCV8U7Dh0r5wDPWJrUdVGdhwNWZvx6_Mh2vh9Kxd1iyAV5jbcbXh67McVHuCl-FBe8-tv30ZYXBrksuKi6_dlwbjhUzfTVmEk6RmwsEjq_hJiBv1K4/s1600/S__5816325.jpg)

<span class="small-text">聽說Python簡單又強大，於是心懷期待，想著可以一步登天，但當面對新問題時，沒有程式設計思路，連問ChatGPT問題都不知道該怎麼問 </span><br>
<span class="small-text">(1) Python 是解問題的工具, 寫程式的核心是「輸入、處理、輸出」，掌握基本框架，才能靈活運用</span>
<span class="small-text">(2) 物件導向編程(OOP)是程式管理和組織的基礎，使程式是有結構、有邏輯，易擴展</span>
<span class="small-text">(3) 解決問題時，好的資料結構和演算法能增進執行效率</span>
<span class="small-text">(4) 有了基礎的邏輯思維和結構設計能力，學習AI/ML或其他高階技能才會事半功倍。</span> 

# Welcome to DSA
- <span class="blue-text">**Data structures**</span>: organize and store information in a program to efficiently manipulate data
- <span class="blue-text">**Algorithm**</span>: set of instructions designed to solve a specific problem

[![Roadmap To Learn Data Structures And Algorithms](https://i.ytimg.com/vi/uZe1Bbsycyc/mqdefault.jpg)](https://youtu.be/uZe1Bbsycyc?si=zcS704k5KTRrkD_u&t=229)


# Why Should I Care About Data Structure
### Solve Lottery by SET or LIST, which data structure is better?
[Code of Lottery](code/lottery.py)

# A Mental Model for Applying Data Structures
![bg right:50% w:80% apply data structure](files/image/a_mental_model_for_applying_data_structures.png)