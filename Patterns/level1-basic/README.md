# 🧩 Level 1 – Basic Patterns

These are simple patterns that help you master **nested loops**, **rows and columns control**, and **printing logic**.

---

## 🟩 [1. Solid Rectangle](solidRectangle.js)

### 🔹 What It Is
A pattern where all rows and columns are completely filled with `*`.

Example for `rows = 3` and `cols = 5`:

### Output

```
*****
*****
*****
```

### 🧮 Complexity Analysis
- **Time Complexity:** O(row × column)  
  > Because there are two nested loops — one for rows and one for columns.
- **Space Complexity:** O(row × column)  
  > Because we store the entire pattern in an array of strings.

  ---
  ## 🟨 [2. Right-Angled Triangle](rightAngledTriangle.js)

### 🔹 What It Is
A pattern where each row adds one more `*` than the previous.

Example for `rows = 4`:

### Output
```
*
**
***
****
*****
```

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > Outer loop runs `n` times, inner loop runs `i` times for each row.
- **Space Complexity:** O(n²)  
  > Because we store the entire pattern (sum of 1 + 2 + ... + n stars).

  ---
  ## 🟥 [3. Right-Angled Numbered Pyramid](rightAngledNumberedPyramid.js)

### 🔹 What It Is
A pattern where each row displays numbers from `1` up to the current row number.

Example for `rows = 5`:

### Output
```
1
12
123
1234
12345
```

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > Outer loop runs `n` times, and the inner loop runs `i` times for each row.
- **Space Complexity:** O(n²)  
  > Each row is stored as a growing string in the pattern array.
