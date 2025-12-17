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
# 資料結構與演算法 (520009)
- 講師：林志偉
- 教材：https://github.com/mingfujacky/Lecture-DSA-2.0.git

# 參考書籍
- 謝樹明, Python 資料結構 X 演算法 刷題鍛鍊班, 旗標出版社, 2022
- Marcello La Rocca, Grokking Data Structures, Manning, 2024

# 課程講師 - 林志偉 (Jacky Lin)
- 現職: 陽明交通大學 / 學士後電子與光子學士學位學程 助理教授
- 學歷: 交大資訊管理博士
- 經歷: 台積電資訊科技(IT)
- 專長: 資料工程、程式設計、巨量資料分析
- Email: jacky.jw.lin@nycu.edu.tw

# 課程助教
蔡孟哲 (aayy0917.sc13@nycu.edu.tw)

# 課程規劃
- #### 課程目標
  - Introduce basic data structures that every programmer needs to know.
  - Use Python to implement basic algorithms to sharpen coding skill.

- #### 授課方式
  - 教材講解 & 課堂實作
  - 課後作業
  - 期中、期末考試
  - 期末專題報告


# 評分方式
- 課堂參與(10%): 5次點名 
  - 正常出席得 2分
  - 有請假單得 1分
  - 無故缺席得 0分
- 課後作業 (30%): 6次作業(遲交不予受理)
- 期中考試 (20%)
- 期末考試 (20%)
- 期末專題 (20%)
  - 口頭報告, 期末考前一週課堂進行
  - 書面報告, 期末考後一週內繳交(遲交不予受理)

# 期中考試與期末考試規定
- 請根據助教指示安排進入考場入座，不得攜帶書本及參考資料
- 考試期間不得使用手機或其他的具通訊功能的設備，請將此種設備放置在監考人員的可視範圍內，如桌上或教室前面
- 攜帶學生證或其他可以確認身份的證件
- 考試時間為六十分鐘

# 期末專題
- 一人一組，主題需與課程相關
- 建議的報告內容包含但不限於:
  - What problem you plan to solve
  - Describe the algorithm and data structure you take to solve the problem
  - Demonstrate code structure and explain major functions
  - Analyze performance
- 參考題目集:
https://docs.google.com/spreadsheets/d/1_VRbVq8M-T5hg49GJxGY-q_SOzCwAgBK8vVqmmurYZ0/edit?gid=994583042#gid=994583042

# 授課大綱
[114下學期](https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=114&Sem=2&CrsNo=520009&lang=zh-tw)

# 時時實際操作
<br>
>我鼓勵你使用鍵盤手動複製這些程式，而不是直接將其原始程式碼複製貼上到新檔案中；這有助於你對程式產生「肌肉記憶」，並迫使你在鍵入時<span class="blue-text">考慮每一行</span>。

![bg right:30% w:300 遞迴演算法大師親授面試心法](https://i3.momoshop.com.tw/1721136961/goodsimg/0013/030/254/13030254_R.jpg)