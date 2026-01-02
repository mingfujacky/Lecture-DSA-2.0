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
# [520009] 資料結構與演算法
## Data Structures and Algorithms (DSA)
> 課程講師：林志偉 (jacky.jw.lin@nycu.edu.tw)
> 課程助教：蔡孟哲 (aayy0917.sc13@nycu.edu.tw)
> 教材網站：https://github.com/mingfujacky/Lecture-DSA-2.0.git
> 上課書籍：Python 資料結構 X 演算法 刷題鍛鍊班, 旗標出版社, 2022
> 參考書籍：Marcello La Rocca, Grokking Data Structures, Manning, 2024

# 課程講師 - 林志偉 (Jacky Lin)
> 現職: 陽明交通大學 / 學士後電子與光子學士學位學程 助理教授
> 學歷: 交大資訊管理博士
> 經歷: 台積電資訊科技(IT)
> 專長: 資料工程、程式設計、巨量資料分析

# 課程目標
> 1. Understand basic data structures like arrays, linked lists, trees and graphs.
> 2. Learn basic algorithms like sorting, searching and traversal.
> 3. Analyze the performance of algorithms using time complexity.
> 4. Implement solutions upon appropriate data structure and algorithm by Python.

# 授課方式
> 1. 課堂講解
> 2. 課間實作
> 3. 課後作業
> 4. 期中考試
> 5. 期末考試
> 6. 期末專題


# 評分方式
- (10%) 課堂參與
  > 5次點名 
  > 正常出席得 2分, 有請假單得 1分, 無故缺席得 0分
- (30%) 課後作業
  > 6次作業 (不受理遲交)
- (20%) 期中考試
- (20%) 期末考試
- (20%) 期末專題
  > 期末考前一週進行口頭報告
  > 期末考後一週繳交書面報告(不受理遲交)

# 試場規定
> 1. 按照助教安排進入考場入座，不得攜帶書本及參考資料
> 2. 不得使用手機，請將手機放置在監考人員的可視範圍內，如桌上或教室前面
> 3. 攜帶學生證或其他可以確認身份的證件
> 4. 考試時間為六十分鐘

# 期末專題
- 一人一組，主題需與課程相關
- 報告內容包含但不限於:
  - Explain the problem you plan to solve
  - Describe the algorithm and data structure you take to solve the problem
  - Demonstrate code structure and explain major functions
  - Analyze performance
- 參考題目集:
https://docs.google.com/spreadsheets/d/1_VRbVq8M-T5hg49GJxGY-q_SOzCwAgBK8vVqmmurYZ0/edit?gid=994583042#gid=994583042

# 授課大綱
[114下學期](https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=114&Sem=2&CrsNo=520009&lang=zh-tw)