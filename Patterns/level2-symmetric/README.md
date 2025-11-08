# 🧩 Level 2 – Intermediate Patterns

These patterns introduce **alignment, spacing, and symmetry** — the next step after mastering basic right-angled structures.

##🧠 1️⃣ Understand What “Symmetry” Means in Patterns

When you see a symmetrical shape, it usually means there’s a mirror axis:

For pyramids → symmetry about the vertical center line

For diamonds → symmetry about both vertical and horizontal centers

So you’re not printing “random stars” — you’re building reflections of left and right halves.

## 💡 Key Idea:

Every symmetrical pattern can be divided into spaces + content (stars/numbers) that mirror around a central axis..

## 🧩 2️⃣ The Golden Rule of Symmetry in Patterns

Spaces make symmetry possible, stars make shape visible.

That’s it.
If you learn to balance spaces before and after your stars, you can center anything — stars, numbers, letters — perfectly.

---

## 🟨 [1. Star Pyramid (Full Pyramid)](starPyramid.js)

### 🔹 What It Is
A centered pyramid pattern made of `*`, where each row contains an odd number of stars and is aligned symmetrically using spaces.

Example for `rows = 5`:

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





