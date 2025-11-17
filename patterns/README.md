# Linked List Problem-Solving Patterns (Python)

This guide contains the **5 most important linked list techniques** used in real LeetCode problems. Each section explains **when to apply the pattern** and includes a clean **Python template**.

## 5 Patterns
1. Fast & Slow Pointers
2. Cycle Detection (Floyd’s Algorithm)
3. Two Pointers With Gap (Nth Node From End) 
4. Reverse a Linked List (In-Place)
5. Dummy Node + Tail Pointer


## ⭐ 1. Fast & Slow Pointers (Floyds Tortoise & Hare)

### Use When:
- Find **middle** of list  
- Detect **cycle**  
- Find **start** of cycle  
- Find **cycle length**  
- Palindrome (first step)

### Template
```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

---

## ⭐ 2. Reverse Linked List (In-Place)

### Use When:
- Reverse entire list  
- Reverse sublist (m → n)  
- Reverse in k-group  
- Palindrome check (reverse second half)  
- Reorder list  

### Template
```
prev = None
curr = head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev
```

---

## ⭐ 3. Two-Pointer Gap Pattern (Nth from End)

### Use When:
- Remove **nth node from end**  
- Find **kth node from end**  
- Alternative method to find middle  

### Template
```
fast moves n+1 steps ahead
then move slow & fast together
slow stops before target
```

---

## ⭐ 4. Dummy Node Technique

### Use When:
- Delete head  
- Insert at head  
- Remove nodes (filtering)  
- Remove duplicates  
- Simplify logic when modifying pointers  

### Template
```
dummy = ListNode(0)
dummy.next = head
curr = dummy
```

---

## ⭐ 5. Dummy + Tail (Build a New List)

### Use When:
- Merge two lists  
- Add two numbers (LeetCode #2)  
- Partition lists  
- Construct filtered/processed list  
- Copy list  

### Template
```
dummy = ListNode(0)
tail = dummy
tail.next = newNode
tail = tail.next
```

---

# 🎯 Pattern Selection Cheat Table

| Problem Asks For… | Best Pattern |
|-------------------|--------------|
| Middle of list | Fast & Slow |
| Detect cycle | Fast & Slow |
| Find start of cycle | Fast & Slow + reset slow |
| Reverse list | In-place reverse |
| Reverse a part | In-place reverse |
| Reverse k-group | Repeated reverse |
| nth from end | Two-pointer gap |
| Delete node | Dummy node |
| Merge lists | Dummy + tail |
| Add two numbers | Dummy + tail + carry |
| Palindrome | Fast & slow + reverse |
| Reorder list | Fast & slow + reverse + merge |

---

