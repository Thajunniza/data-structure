# Data-Structure
- Data structures are the way of organizing and storing the data or info in a computer or in a program which helps to efficiently mangae and manipulate data.
- It defines the relationship between the data elements, the operations that
can be performed, and the rules or constraints for accessing and modifying the data.
- A Data Structure is the way of orginizing data so that it can be used effectively.
- Essential ingredients to creating fast and powerful algorithms.
- makes code cleaner and easier to understand.
- good code results in great product.

## Algorithm
- An algorithm is a set of well-defined instructions, a step-by-step procedure designed
to solve a specific problem or perform a particular task.
- Algorithms are used to describe the operations performed on data
structures.
- To use an analogy, data structures are like nouns, while algorithms
are more like verbs.

## Data Structure and Algorithm
- Data structures and algorithms are interdependent.
- Data structures provide the organization and representation of information (the data),
and algorithms serve as instructions for transforming that data. Each data structure
implicitly defines algorithms for operations, such as adding, retrieving, and removing its
elements.

## Why Data Structure 
- DS are the building blocks of Computer science.
- helps to organize data
- solve difficult problem
- improve the efficiency
- optimize memory usage
- avoid security risk

## How do we use DS:
![alt text](image.png)

# 🧩 Types of Data Structure

Data Structures are ways to store and organize data efficiently in memory.  
They are broadly classified into two main types:

1. **Primitive Data Structures**  
2. **Non-Primitive Data Structures**

---

## 🟩 Primitive Data Structure

- Basic data types and can’t be broken into simpler data types  
- Act as **basic building blocks**  
- Store a **single value**  
- **Fixed and smaller** in size  
- Represented in memory as **simple values**

### 🔹 Types of Primitive Data Structures

| Type  | Description | Example |
|-------|--------------|----------|
| **int** | Stores integers | `x = 10` |
| **float** | Stores decimal numbers | `pi = 3.14` |
| **bool** | Stores True/False values | `is_active = True` |
| **str** | Stores text (sequence of characters) | `name = "Thaj"` |

---

## 🟦 Non-Primitive Data Structure

- **Complex data types** built from primitive ones  
- Can be broken into simpler data types  
- **Larger in size** and can grow or shrink dynamically  
- Represented in memory as **pointers or references** to other locations

### 🔹 Types of Non-Primitive Data Structures

---

### **(a) Linear Data Structures**

Data is arranged **in a sequence** — one after another.

| Type | Description | Example |
|------|--------------|----------|
| **List** | Mutable, ordered collection | `[1, 2, 3]` |
| **Tuple** | Immutable, ordered collection | `(1, 2, 3)` |
| **Stack** | LIFO (Last In, First Out) structure | `push(), pop()` |
| **Queue** | FIFO (First In, First Out) structure | `enqueue(), dequeue()` |
| **Array** | Fixed-type elements (using `array` module) | `array('i', [1, 2, 3])` |

---

### **(b) Non-Linear Data Structures**

Data is **not arranged sequentially**, but **hierarchically** or in **networks**.

| Type | Description | Example |
|------|--------------|----------|
| **Set** | Unordered, unique values | `{1, 2, 3}` |
| **Dictionary (Hash Map)** | Key–Value pairs | `{'a': 1, 'b': 2}` |
| **Tree** | Hierarchical structure | `Binary Tree`, `BST` |
| **Graph** | Nodes connected by edges | Social network model |

---

## 🧠 Summary

| Category | Examples | Structure |
|-----------|-----------|------------|
| **Primitive** | int, float, bool, str | Single value |
| **Non-Primitive (Linear)** | List, Tuple, Stack, Queue, Array | Sequential |
| **Non-Primitive (Non-Linear)** | Set, Dict, Tree, Graph | Hierarchical / Network |

---

> 💡 **Tip:**  
> Start with Python’s built-in structures (`list`, `tuple`, `set`, `dict`) before diving into advanced structures like `stack`, `queue`, or `tree`.

# ⚙️ Types of Algorithms

An **algorithm** is a **step-by-step procedure** to solve a problem or perform a task efficiently.  
Algorithms can be categorized based on their **design techniques** and **problem-solving purpose**.

---

## 🧩 1️⃣ Based on Design / Approach

| Type | Description | Example Problems |
|------|--------------|------------------|
| **Brute Force Algorithm** | Tries **all possible solutions** until the correct one is found. Simple but inefficient for large inputs. | Linear Search, Trial Division |
| **Divide and Conquer** | Breaks a problem into smaller subproblems, solves them recursively, and combines the results. | Merge Sort, Quick Sort, Binary Search |
| **Greedy Algorithm** | Makes the **locally optimal** choice at each step, hoping to find a global optimum. | Kruskal’s, Prim’s, Huffman Coding |
| **Dynamic Programming (DP)** | Breaks problems into overlapping subproblems and **stores intermediate results** to avoid recomputation. | Fibonacci Series, Knapsack Problem |
| **Backtracking** | Builds a solution step by step and **abandons a path** when it’s not feasible. | N-Queens, Sudoku Solver |
| **Recursion** | Solves problems by **calling itself** with smaller inputs until a base condition is reached. | Factorial, Tower of Hanoi |
| **Randomized Algorithm** | Uses **random numbers** to make decisions within logic. Often used for optimization. | QuickSort (random pivot), Monte Carlo Method |
| **Branch and Bound** | Explores all possible solutions but **prunes** paths that cannot yield better results. | Travelling Salesman Problem (TSP) |

---

## 🧱 2️⃣ Based on Functionality / Purpose

| Category | Description | Example Algorithms |
|-----------|--------------|--------------------|
| **Searching Algorithms** | Used to find an element in a data structure. | Linear Search, Binary Search |
| **Sorting Algorithms** | Arranges data in a particular order (ascending/descending). | Bubble Sort, Merge Sort, Quick Sort |
| **Graph Algorithms** | Used to solve graph-related problems. | BFS, DFS, Dijkstra’s, Kruskal’s |
| **String Algorithms** | Focused on pattern matching and text processing. | KMP, Rabin-Karp, Z Algorithm |
| **Numerical Algorithms** | Deal with mathematical and numerical computations. | GCD, Fast Exponentiation |
| **Optimization Algorithms** | Used to find the best possible solution from many. | Dynamic Programming, Linear Programming |
| **Machine Learning Algorithms** | Used to learn from data and make predictions. | Decision Tree, K-Means, Neural Networks |



---
## Abstract Data Type
- ADT is conceptual model that defines and classify data structure based on how they are used and what they provide.
- They dont specify about how the data structure is implemented or in what programming language they follow.

### Example of ADT
| **Abstract Data Type (ADT)** | **Conceptual Description (What it does)** | **Common Implementations (How it's built)** |
|------------------------------|-------------------------------------------|---------------------------------------------|
| **List**                    | A sequential collection of elements accessible by index. | Array (or Dynamic Array/ArrayList), Linked List (Singly or Doubly Linked) |
| **Stack**                   | A Last-In, First-Out (LIFO) collection, like a stack of plates. | Array, Linked List |
| **Queue**                   | A First-In, First-Out (FIFO) collection, like people in a line. | Array, Linked List |
| **Set**                     | An unordered collection of unique elements. | Hash Table (or HashSet), Binary Search Tree (BST), Sorted Array |
| **Map (Dictionary)**        | Stores key-value pairs, allowing retrieval by unique key. | Hash Table (or HashMap), Binary Search Tree (or TreeMap), Balanced Tree (e.g., Red-Black Tree) |
| **Priority Queue**          | A collection where elements are removed based on priority, not insertion order. | Heap (often implemented using an Array), Binary Search Tree |
| **Graph**                   | A collection of nodes (vertices) and connections (edges). | Adjacency Matrix, Adjacency List (using an Array of Linked Lists or Hash Maps) |
| **Tree**                    | A hierarchical structure of nodes. | Linked Nodes (using pointers/references), Array (especially for complete trees like Heaps) |




## 📝 Topics
- 📊 [Arrays](./Arrays/)
- 🔗 [Linked Lists](./Linked-Lists/)
- 🧱 [Stacks](./Stacks/)
- 📥 [Queues](./Queues/)
- 🧮 [Hash Tables](./Hash-Tables/)
- 🌳 [Trees](./Trees/)
- 🌲 [Binary Search Trees](./Binary-Search-Trees/)
- ⛰️ [Heaps](./Heaps/)
- 🕸️ [Graphs](./Graphs/)
- 🔤 [Trie](./Trie/)
- 🧬 [Union Find](./Union-Find/)

## 📺 YouTube Playlists
- [William Fiset's Data Structure Playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)
- [](https://www.youtube.com/watch?v=O9v10jQkm5c)

## Courses
-[Coursera Data Structure](https://www.coursera.org/programs/aptiv-integration-intended-l5k7z/learn/data-structures?authProvider=aptiv)
-[Python] (https://www.coursera.org/learn/python-data)
