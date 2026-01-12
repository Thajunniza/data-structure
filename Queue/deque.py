"""
===========================================================
Deque (Double-Ended Queue) Demonstration using collections
===========================================================

Description:
------------
This script demonstrates the usage of Python's `collections.deque`,
a highly optimized double-ended queue data structure that supports
O(1) insertions and deletions from both ends.

The example covers common deque operations such as:
    • appending elements
    • removing elements
    • accessing front elements
    • extending the deque
    • rotation and reversal

Why deque?
----------
`deque` is preferred over list when frequent insertions or removals
are required at both the front and rear of the collection.

Key Properties:
---------------
    • FIFO and LIFO behavior supported
    • Thread-safe for appends and pops
    • Faster than list for queue operations

Operations Demonstrated:
------------------------
    • append(x)        : Add element to the right end
    • appendleft(x)   : Add element to the left end
    • pop()           : Remove element from the right end
    • popleft()       : Remove element from the left end
    • insert(i, x)    : Insert element at index i
    • extend(iter)    : Extend deque on the right
    • extendleft(iter): Extend deque on the left (reversed order)
    • remove(x)       : Remove first occurrence of value
    • count(x)        : Count occurrences of value
    • rotate(n)       : Rotate deque n steps to the right
    • reverse()       : Reverse elements in place

Time Complexity:
----------------
    • append / appendleft   : O(1)
    • pop / popleft        : O(1)
    • rotate               : O(k)
    • insert / remove      : O(n)

Use Cases:
----------
    • Queue and Stack implementations
    • Sliding window problems
    • BFS / Level-order traversal
    • Real-time data buffering

Author:
-------
    Thajunniza M A

===========================================================
"""


import collections as c

dq = c.deque()

dq.append(5)
dq.append(6)
print(dq)

dq.appendleft(1)
dq.appendleft(2)
print(dq)

print(dq[0])
print(len(dq))

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.insert(1,10)
print(dq)

dq.extend([11,12,13])
print(dq)

dq.extendleft([5,55,555])
print(dq)

dq.remove(55)
print(dq)
print(dq.count(5))

dq.rotate(3)
print("Rotate the deque 3 times to the right: ", list(dq))

dq.reverse()
print("Reverse the deque: ", list(dq))