# 🧠 Fast & Slow Pointer Pattern — Problem Guide

This README collects **key problems that use the Fast & Slow Pointer (Tortoise & Hare) pattern**, and explains **how** the pattern is applied in each.

Fast & Slow is *one pattern* with several classic use-cases:

- Find the **middle** of a linked list  
- **Detect** if there is a cycle  
- Find the **start** of a cycle  
- Sometimes used on arrays / numbers (cycle in state space)

---

## 🚩 Core Template

```python
slow = fast = head

while fast and fast.next:
    slow = slow.next          # 1 step
    fast = fast.next.next     # 2 steps
```

Variations:
- Stop when `fast` reaches end → **middle of list**
- Stop when `slow == fast` → **cycle detected**
- After meeting, reset one pointer → **start of cycle**

---

## 📂 Category 1 — Find Middle of Linked List

### 🔹 Problem: Middle of the Linked List (LeetCode 876)
- **Type:** Singly linked list
- **Goal:** Return the **middle node**. If even length, return the **second** middle.
- **Pattern Use:**
  - Use fast & slow.
  - When `fast` reaches the end, `slow` is at the middle.

**Pseudo:**

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

---

### 🔹 Problem: Palindrome Linked List (LeetCode 234)
- **Type:** Singly linked list
- **Goal:** Check if list reads the same forward and backward.
- **Pattern Use:**
  1. Use **fast & slow** to find middle.
  2. Reverse second half of list.
  3. Compare first half and reversed second half.

Fast & slow is used for **splitting the list into two halves**.

---

### 🔹 Problem: Reorder List (LeetCode 143)
- **Type:** Singly linked list
- **Goal:** Reorder L0 → Ln → L1 → Ln-1 → … in-place.
- **Pattern Use:**
  1. **Find middle** via fast & slow.
  2. **Reverse** the second half.
  3. **Merge** two lists alternately.

Fast & slow is used in step 1.

---

## 📂 Category 2 — Detect Cycle

### 🔹 Problem: Linked List Cycle (LeetCode 141)
- **Type:** Singly linked list
- **Goal:** Detect if the list has a **cycle** (True/False).
- **Pattern Use:**
  - fast moves 2 steps, slow moves 1 step.
  - If they ever meet → cycle exists.
  - If `fast` or `fast.next` hits `None` → no cycle.

**Pseudo:**

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

This is the classic **Floyd’s Cycle Detection Algorithm**.

---

### 🔹 Problem: Happy Number (LeetCode 202)
- **Type:** Number / math, not a linked list
- **Goal:** Determine if repeatedly summing squares of digits ends at 1 or loops forever.
- **Pattern Use:**
  - Treat the sequence of values as a “linked” state space.
  - Use fast & slow to detect **cycle in values**.

**Idea:**
- slow: apply function once
- fast: apply function twice
- If they meet at 1 → happy
- If they meet at another number repeatedly → cycle, not happy

---

### 🔹 Problem: Find the Duplicate Number (LeetCode 287)
- **Type:** Array
- **Goal:** Find the single duplicate number without modifying the array, using O(1) extra space.
- **Pattern Use:**
  - Treat array indices & values as a **linked structure**:
    - `next = nums[index]`
  - Use fast & slow to detect cycle and its entry.
  - The entry point of the cycle = duplicate number.

Although not a linked list, it uses the same cycle detection concept.

---

## 📂 Category 3 — Find Start of Cycle

### 🔹 Problem: Linked List Cycle II (LeetCode 142)
- **Type:** Singly linked list
- **Goal:** Return the **node where the cycle begins** (or None if no cycle).
- **Pattern Use:** Two-phase fast & slow.

**Steps:**
1. First, run normal cycle detection:
   - If `slow` and `fast` never meet → no cycle (return None).
   - If they meet, there **is** a cycle.
2. Reset one pointer to head:
   - `slow = head`
3. Move both pointers **one step at a time**:
   - The node where they meet again = **start of cycle**.

**Pseudo:**

```python
# phase 1: detect cycle
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        break
else:
    return None   # no cycle

# phase 2: find entry
slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next

return slow
```

---

### 🔹 Problem: Find the Duplicate Number (LeetCode 287) — again
In the array version:
- The **meeting point** corresponds to inside the cycle.
- Reset one pointer to the “head” index (0).
- Move both 1 step at a time using `index = nums[index]`.
- The index/value where they meet = duplicate.

Same **start-of-cycle** logic.

---

## 📂 Category 4 — Mixed / Advanced Problems Using Fast & Slow

These problems combine fast & slow with **reversal**, **merging**, or **dummy nodes**:

- **Palindrome Linked List (LeetCode 234)**  
  - Fast & slow for middle  
  - Reverse for second half  
  - Comparison for palindrome

- **Reorder List (LeetCode 143)**  
  - Fast & slow for middle  
  - Reverse to flip second half  
  - Merge alternating nodes

- **Sort List (LeetCode 148)**  
  - Uses **merge sort** on linked list  
  - Fast & slow to split list into halves recursively

These show that **Fast & Slow is often just the first step** of bigger patterns.

---

## 🧾 Summary Table

| Use-Case            | Example Problems                            | Key Idea                          |
|---------------------|---------------------------------------------|-----------------------------------|
| Find middle         | Middle of Linked List, Palindrome, Reorder | Stop when fast reaches end        |
| Detect cycle        | Linked List Cycle, Happy Number             | Check if slow == fast at any time |
| Find cycle start    | Linked List Cycle II, Find Duplicate Number| Reset one pointer, step together  |
| Split list in half  | Reorder List, Sort List                     | Use slow as midpoint              |

---

## ✅ How to Practice This Pattern

1. **Start with Linked List problems:**
   - Middle of Linked List (876)
   - Linked List Cycle (141)
   - Linked List Cycle II (142)

2. Then move to **mixed patterns:**
   - Palindrome Linked List (234)
   - Reorder List (143)

3. Finally try **non-linked-list uses:**
   - Happy Number (202)
   - Find the Duplicate Number (287)

If you master these, you’ll be fully comfortable with the **Fast & Slow Pointer Pattern** in interviews.
