# 🧩 Level 2 – Symmetric Patterns

These patterns introduce **alignment, spacing, and symmetry** —  
the next step after mastering basic right-angled structures in Level 1.

---

## 🧠 Understanding Symmetry in Patterns

When you see a **symmetrical shape**, it usually means there’s a **mirror axis**:

- For **pyramids** → symmetry about the **vertical center line**  
- For **diamonds** → symmetry about both **vertical and horizontal** centers  

You’re not printing “random stars” —  
you’re building **reflections** of the left and right halves using spaces and stars (or numbers).

---

### 💡 Key Idea
> Every symmetrical pattern can be divided into **spaces + content** (stars/numbers)  
> that mirror around a **central axis**.

---

### 🧩 The Golden Rule of Symmetry
> **Spaces make symmetry possible, stars make shape visible.**

If you learn to **balance spaces before and after your stars**,  
you can center anything — stars, numbers, or letters — perfectly.

---

## 🟨 [1. Star Pyramid (Full Pyramid)](starPyramid.js)

### 🔹 What It Is
A centered pyramid pattern made of `*`,  
where each row contains an odd number of stars and is aligned symmetrically using spaces.

**Example for `rows = 5`:**


### Output
````
    *
   ***
  *****
 *******
*********
````


### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > For each of the `n` rows, we compute both spaces and stars — the total work grows quadratically with rows.
- **Space Complexity:** O(n²)  
  > The full pattern is stored in an array of strings, each containing spaces and stars.
 - “In each row, the number of characters printed (spaces + stars) grows linearly with rows.
Since we repeat that for every row, the total number of operations is roughly proportional to the sum of the first n integers — which gives O(n²).
Similarly, since we store each row, the space complexity is also O(n²).” 

## 🟧 [2. Inverted Star Pyramid (Inverted Full Pyramid)](invertedStarPyramid.js)

### 🔹 What It Is
A mirror image of the Full Star Pyramid — it starts with the maximum number of `*` in the first row and decreases by two stars on each subsequent row, forming an inverted centered triangle.

Example for `rows = 5`:

### Output
````
*********
 *******
  *****
   ***
    *
````

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > The outer loop runs `n` times.  
  > For each row, we handle both spaces and stars whose combined total is proportional to `n`, leading to a quadratic runtime overall.
- **Space Complexity:** O(n²)  
  > Each row (containing spaces and stars) is stored in an array, and total characters across all rows sum up to O(n²).


## 🟪 [3. Diamond Star Pattern](diamondStarPattern.js)

### 🔹 What It Is
A symmetrical pattern made by combining a **Full Star Pyramid** (increasing stars) and an **Inverted Star Pyramid** (decreasing stars).  
It forms a perfect diamond shape with a vertical axis of symmetry.

Example for `rows = 5`:

### Output
````
   *
  ***
 *****
*******
 *****
  ***
   *
`````

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > The diamond consists of two pyramids (one upright and one inverted).  
  > Each part individually runs in O(n²), and combining them still results in O(n²).
- **Space Complexity:** O(n²)  
  > Each row (spaces + stars) is stored as a string, and total characters across all rows grow quadratically with `n`.


## 🟫 [4. Half Diamond Star Pattern](halfDiamondStarPattern.js)

### 🔹 What It Is
A pattern that forms a diamond shape split vertically in half.  
It first increases the number of `*` per row (like a right-angled triangle) and then decreases, creating a half-diamond shape.

Example for `rows = 5`:

### Output
````
*
**
***
****
*****
****
***
**
*
````


### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > The pattern is composed of two right-angled triangles (one increasing, one decreasing).  
  > Both parts together still have quadratic growth in total operations.
- **Space Complexity:** O(n²)  
  > Each row is stored as a string, and the sum of all characters printed grows quadratically with the number of rows.


## 🟩 [5. Binary Number Triangle Pattern](binaryNumberTrianglePattern.js)

### 🔹 What It Is
A right-angled triangle pattern made of alternating binary digits (`0` and `1`).  
Each row starts with `1` if the row number is odd, or `0` if the row number is even — and alternates thereafter.

Example for `rows = 5`:

### Output
1
01
101
0101
10101


### 🧮 Logic Breakdown
- Each row number `i` determines the **starting bit**:
  - If `i` is odd → start with `1`
  - If `i` is even → start with `0`
- Within a row, bits alternate (`0 → 1 → 0 → 1 …`).

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > Outer loop runs `n` times; inner loop runs up to `i` times, totaling ~n² operations.
- **Space Complexity:** O(n²)  
  > Each row (string of binary digits) is stored; total grows quadratically with `n`.

---
## 🟪 [6. Number Crown Pattern](numberCrownPattern.js)

### 🔹 What It Is
A **symmetrical numeric pattern** that looks like a crown 👑.  
Each row contains an increasing sequence of numbers on the left and a decreasing sequence on the right,  
with a central gap that gets smaller in each row — forming a perfectly balanced crown-like structure.

**Example for `rows = 5`:**
1        1
12      21
123    321
1234  4321
1234554321


### 🧮 Logic Breakdown
- For each row `i`:
  1. Print **ascending numbers** → `1` to `i`
  2. Print **spaces** → `2 × (rows - i)` spaces
  3. Print **descending numbers** → `i` to `1`
- As `i` increases:
  - The **spaces shrink by 2** per row.
  - The numbers grow outward symmetrically from the center.

---

### 🧠 Example Breakdown for `rows = 5`

| Row | Left Numbers | Spaces | Right Numbers | Output |
|------|---------------|---------|----------------|---------|
| 1 | 1 | 8 | 1 | `1        1` |
| 2 | 12 | 6 | 21 | `12      21` |
| 3 | 123 | 4 | 321 | `123    321` |
| 4 | 1234 | 2 | 4321 | `1234  4321` |
| 5 | 12345 | 0 | 54321 | `1234554321` |

---

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > For each of the `n` rows, we print ascending numbers, spaces, and descending numbers —  
  resulting in total operations proportional to `n²`.
- **Space Complexity:** O(n²)  
  > Each row (numbers + spaces) is stored as a string → total memory usage grows quadratically with `n`.

---

### 🧩 Key Learnings
- Reinforces **mirror symmetry** using numbers.  
- Great practice for **string concatenation** and **space management**.  
- Introduces the concept of **shrinking center gaps** — a common trick for centered symmetric patterns.

---



---

## 🧩 Summary

| # | Pattern Name | Concept Focus | Symmetry Type |
|---|---------------|----------------|----------------|
| 1️⃣ | Star Pyramid | Center alignment | Vertical |
| 2️⃣ | Inverted Star Pyramid | Reverse symmetry | Vertical |
| 3️⃣ | Diamond Star Pattern | Combined mirror logic | Vertical + Horizontal |
| 4️⃣ | Half Diamond Star Pattern | Dual triangular reflection | Vertical |
| 5️⃣ | Binary Number Triangle | Alternating logic pattern | Left-aligned |
| 6️⃣ | Number Crown Pattern | Numeric mirror with shrinking space | Vertical |

---

## ✨ Key Takeaways
- All patterns use **nested loops** — outer loop for rows, inner loop for columns/spaces.
- Symmetry is achieved by **balancing spaces** and **content (stars/numbers)**.
- Perfect for strengthening **logical reasoning** and **pattern visualization** skills.

---




