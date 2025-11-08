# 🎨 Understanding Pattern Problems

## 💡 What is a Pattern Problem?
Loop is the main concept of Coding.
A **pattern problem** is a coding exercise where you print specific **shapes, numbers, or designs** (like triangles, pyramids, diamonds, etc.) using **loops**.

You’re not doing it for the output’s beauty — you’re doing it to **train your brain to think logically** and understand **how loops, conditions, and variables work together**.

---

## 🧠 Why You Need It
Before diving into Data Structures & Algorithms (DSA), you must first be comfortable with:
- Breaking a problem into smaller logical steps  
- Using nested loops effectively  
- Managing indexes, spaces, and print conditions  
- Visualizing how code executes line by line  

Practicing pattern problems builds these core skills — the same logic later helps with arrays, matrices, recursion, and other DSA concepts.

---
## Rules to Follow while Pattern design.
- All patterns will have nested loops- Outer loops and inner loops
- Outer loops are rows and Iner loops are columns.
- For the Outer loop count the number of rows/lines.
- For the Inner loop foucus on the columns and try to connect to the outerloops which is rows.
- Print them inside the inner loop
- Obeserve Symmentry (Optional)
- We always use nested loops for printing the patterns. For the outer loop, we count the number of lines/rows and loop for them.
- Next, for the inner loop, we focus on the number of columns and somehow connect them to the rows by forming a logic such that for each row we get the required number of columns to be printed.

---
# 🌟 JavaScript Pattern Problems

> A complete collection of **pattern printing problems** solved in **JavaScript**, organized by levels —  
from basic loops to advanced symmetrical logic — to strengthen your **DSA fundamentals** and **loop control**.

---

## 🧭 Categories Overview

| Level | Focus | Example Patterns |
|--------|--------|------------------|
| 🟩 **Level 1 – Basic Patterns** | Fundamental loop control & 2D iteration | Rectangles, Right Triangles |
| 🟦 **Level 2 – Symmetric Patterns** | Space management & mirroring logic | Pyramids, Diamonds, Crowns |
| 🟥 **Level 3 – Advanced Number Patterns** *(coming soon)* | Mathematical & centered numeric logic | Pascal’s Triangle, Palindromes |
| 🟧 **Level 4 – Hollow / Complex Patterns** *(coming soon)* | Combining conditions, spacing & logic | Hollow Diamonds, Hourglass |

---

## 🟩 [Level 1 – Basic Patterns](./level1-basic/README.md)
> Learn how nested loops work by controlling **rows** and **columns**.

| # | Pattern Name | File Link |
|---|---------------|-----------|
| 1️⃣ | Solid Rectangle | [solidRectangle.js](./level1-basic/solidRectangle.js) |
| 2️⃣ | Right-Angled Triangle | [rightAngledTriangle.js](./level1-basic/rightAngledTriangle.js) |
| 3️⃣ | Right-Angled Number Pyramid I | [rightAngledNumberPyramid.js](./level1-basic/rightAngledNumberPyramid.js) |
| 4️⃣ | Right-Angled Number Pyramid II | [rightAngledNumberPyramidII.js](./level1-basic/rightAngledNumberPyramidII.js) |
| 5️⃣ | Inverted Right-Angled Triangle | [invertedRightAngledTriangle.js](./level1-basic/invertedRightAngledTriangle.js) |
| 6️⃣ | Inverted Numbered Right-Angled Pyramid | [invertedNumberedRightAngledPyramid.js](./level1-basic/invertedNumberedRightAngledPyramid.js) |
| 7️⃣ | Binary Number Triangle Pattern | [binaryNumberTrianglePattern.js](./level1-basic/binaryNumberTrianglePattern.js) |

---

## 🟦 [Level 2 – Symmetric Patterns](./level2-symmetric/README.md)
> Focuses on **symmetry**, **alignment**, and **space handling** using nested loops.

| # | Pattern Name | File Link |
|---|---------------|-----------|
| 1️⃣ | Full Star Pyramid | [starPyramid.js](./level2-symmetric/starPyramid.js) |
| 2️⃣ | Inverted Star Pyramid | [invertedStarPyramid.js](./level2-symmetric/invertedStarPyramid.js) |
| 3️⃣ | Diamond Star Pattern | [diamondStarPattern.js](./level2-symmetric/diamondStarPattern.js) |
| 4️⃣ | Half Diamond Star Pattern | [halfDiamondStarPattern.js](./level2-symmetric/halfDiamondStarPattern.js) |
| 5️⃣ | Number Crown Pattern | [numberCrownPattern.js](./level2-symmetric/numberCrownPattern.js) |

---

## 🟥 Level 3 – Advanced Number Patterns *(Coming Soon)*

| # | Pattern Name | Description |
|---|---------------|-------------|
| 1️⃣ | Pascal’s Triangle | Classic combination-based numeric pyramid |
| 2️⃣ | Centered Number Pyramid | Symmetrical number pyramid (e.g., 1 22 333) |
| 3️⃣ | Palindromic Number Pyramid | Numbers mirror around the center |
| 4️⃣ | Increasing-Decreasing Number Sequence | Expanding + shrinking numeric series |

---

## 🟧 Level 4 – Hollow / Complex Patterns *(Coming Soon)*

| # | Pattern Name | Description |
|---|---------------|-------------|
| 1️⃣ | Hollow Star Pyramid | Outline-only pyramid pattern |
| 2️⃣ | Hollow Diamond | Space-centered hollow diamond |
| 3️⃣ | Hourglass Pattern | Inverted + upright combined symmetry |
| 4️⃣ | Butterfly Pattern | Wing-like symmetrical structure |

---

## ⚙️ How to Run

Run any pattern file directly with Node.js:

```bash
node level1-basic/rightAngledTriangle.js


