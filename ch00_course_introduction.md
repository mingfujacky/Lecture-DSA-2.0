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
    font-size: 0.50rem;
  }
---
# 資料結構與演算法
- 講師：林志偉
- 教材：https://github.com/mingfujacky/Lecture-Data-Structure.git
![bg right:30% w:300 Data Structure Material in Git](files/image/qrcode_lecture_data_structure.png)

# Textbook
![bg right:60% w:50% textbook](files/image/cover_textbook.jpg)
- Grokking Data Structures
- La Rocca, Marcello
- Manning, 2024

# 課程講師 - 林志偉 (Jacky Lin)
![bg right:30% w:300](files/image/jacky_last_day_in_tsmc.jpg)

- #### 現職: 陽明交通大學 / 學士後電子與光子學士學位學程 助理教授
- #### 學歷: 交大資訊管理博士
- #### 經歷: 台積電資訊科技(IT)
- #### 專長: 資料工程、程式設計、巨量資料分析
- #### Email: jacky.jw.lin@nycu.edu.tw

# 課程助教
蔡孟哲 (aayy0917.sc13@nycu.edu.tw)

# 課程規劃
- #### 課程目標
  *-* Introduce basic data structures that every programmer needs to know.
  *-* Use Python to implement basic algorithms to sharpen coding skill.

- #### 授課方式
  - 教材講解
  - 課堂 Lab 實作 (上課請攜帶電腦)
  - Deliver final project in group (<=3 members) or individual. The project topic is related to data structures and algorithms. For example,
    - 成績管理系統 / 圖書管理系統 / 井字遊戲 / Undo-redo
    - 迷宮 / Huffman 編碼 / 排序演算法比較 / 抄襲檢測 / 社交網路分析


# 評分方式
- Attendance(10%): 5 roll calls 
  - 2 points for full attendance
  - 1 point for excused absence (with approved leave)
  - 0 point for unexcused absence
- Homework (30%): 6 assignments will be given (late submissions will not be accepted)
- Mid-term exam (20%): closed-book written exam @ 10/31
- Final-term exam (20%): closed-book written exam @ 12/19
- Project (20%): live demo + algorithm explanation + complexity analysis
  - (10%) Final report oral presentation @ 12/12
  - (10%) Submit final written report @ 12/26 (don't be late)

# 期中期末考試規定
- 請根據助教指示安排進入考場入座，不得攜帶書本及參考資料
- 考試期間不得使用手機或其他的具通訊功能的設備，請將此種設備放置在監考人員的可視範圍內，如桌上或教室前面
- 攜帶學生證或其他可以確認身份的證件
- 考試時間為六十分鐘  

# Final Report
- Recommend TOC
  - What problem you plan to solve
  - Describe the algorithm and data structure you take to solve the problem
  - Demonstrate code structure and explain major functions
  - Show testing result
  - Analyze performance
- Final project oral presentation: 12/12, 10 minutes per person
- Final project written report: 12/26 23:59
- Candidates
https://docs.google.com/spreadsheets/d/1_VRbVq8M-T5hg49GJxGY-q_SOzCwAgBK8vVqmmurYZ0/edit?gid=994583042#gid=994583042

# 授課大綱
[114上學期](https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=114&Sem=1&CrsNo=520016&lang=)

# 時時實際操作
<br>
>我鼓勵你使用鍵盤手動複製這些程式，而不是直接將其原始程式碼複製貼上到新檔案中；這有助於你對程式產生「肌肉記憶」，並迫使你在鍵入時<span class="blue-text">考慮每一行</span>。

![bg right:30% w:300 遞迴演算法大師親授面試心法](https://i3.momoshop.com.tw/1721136961/goodsimg/0013/030/254/13030254_R.jpg)