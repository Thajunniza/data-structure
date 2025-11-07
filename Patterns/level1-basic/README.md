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

## 🟫 [4. Right-Angled Number Pyramid – II](rightAngledNumberPyramidII.js)

### 🔹 What It Is
A variation of the numbered right-angled pyramid where each row prints the **current row number**, repeated the same number of times as the row itself.

Example for `rows = 5`:

### Output
````
1
22
333
4444
55555
````

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > Outer loop runs `n` times; inner loop runs `i` times for each row to print the row number repeatedly.
- **Space Complexity:** O(n²)  
  > Each row is stored as a string with a length equal to its row number.

## 🟦 [5. Inverted Right-Angled Pyramid](invertedRightAngledPyramid.js)

### 🔹 What It Is
A pattern that starts with the maximum number of `*` in the first row and decreases by one `*` in each subsequent row, forming an inverted right-angled shape.

Example for `rows = 5`:

### Output
````
*****
****
***
**
*

````

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > Outer loop runs `n` times, and the inner loop runs decreasing iterations (`n`, `n-1`, ..., `1`), which still sums up to O(n²).
- **Space Complexity:** O(n²)  
  > Each row is stored as a string of decreasing length.

## 🟩 [6. Inverted Numbered Right-Angled Pyramid](invertedNumberedRightAngledPyramid.js)

### 🔹 What It Is
A pattern that starts with numbers from `1` up to the row count in the first row, and then decreases by one number in each subsequent row, forming an inverted right-angled shape.

Example for `rows = 5`:

### Output
````
12345
1234
123
12
1
````

### 🧮 Complexity Analysis
- **Time Complexity:** O(n²)  
  > Outer loop runs `n` times, and the inner loop runs decreasing iterations (`n`, `n-1`, ..., `1`), totaling O(n²) operations.
- **Space Complexity:** O(n²)  
  > Each row is stored as a string, with the total number of digits across rows summing up to O(n²).



