# Linked List

Linked Lists are fundamental data structures in computer science. Unlike arrays, they don’t require a predefined size and grow dynamically as elements are added. Each element points to the next, allowing efficient insertions and deletions without shifting elements.

---

## 1. What is a Linked List?

A linked list is a linear data structure made up of **nodes**. Each node contains:

- **Data**: the value stored
- **Next Pointer**: reference to the next node

The last node points to **null**, indicating the end of the list. Nodes may be scattered in memory; pointers keep them connected.

---

## Types of Linked Lists

- **Singly Linked List**
- **Doubly Linked List**
- **Circular Linked List**

---

## Structure of a Node

Each node contains:

- **Data** — stored element  
- **Next** — pointer to the next node  

![alt text](image.png)

---

## Arrays vs Linked Lists

![alt text](image-1.png)

---

## 1. Singly Linked List

A singly linked list node contains:

- A value  
- A pointer to the **next** node  

### Characteristics

- Traversal is forward-only (head → tail)
- Simple and memory efficient
- Cannot traverse backward
- Finding a previous node requires starting from the head

### When to Use

- Forward traversal problems  
- Memory efficiency  
- Frequent insert/delete operations in the middle or head  

---

## Operations on Linked Lists

### 1. Traversal  
Move through the list node-by-node starting at the head until `null`.  
**Time Complexity: O(n)**

### 2. Search  
Check every node from head until the value is found or reach the end.  
**Time Complexity: O(n)**

---

## 2. Doubly Linked List

Each node has:

- **prev pointer**  
- **next pointer**

### Advantages

- Bidirectional traversal  
- Efficient deletion from both ends  

### Disadvantages

- More memory due to extra pointer  

---

## 3. Circular Linked List

The last node points back to the **head**, forming a loop.

### Uses

- Round-robin scheduling  
- Repeated cycling tasks  
- Multiplayer turn-based systems  

---

## Common Interview Patterns

### 1. Fast & Slow Pointers (Floyd’s Algorithm)
Used for:

- Cycle detection  
- Middle-of-linked-list  
- Finding cycle length  

### 2. In-Place Reversal
Reverse pointer direction using three pointers (prev, curr, next).

### 3. Dummy Node Trick
A dummy node simplifies operations like inserting or deleting at head.  
It removes edge-case handling and makes code cleaner.
Use when:
- Removing nodes (especially at head)
- Inserting before head
- Filtering nodes (remove all with value X)
- Merging lists and returning a new list

---

## Time Complexity Summary

| Operation | Complexity |
|----------|------------|
| Access by index | O(n) |
| Search | O(n) |
| Insert at head | O(1) |
| Insert at tail | O(1) with tail pointer, else O(n) |
| Delete head | O(1) |
| Delete tail | O(n) in singly, O(1) in doubly |
