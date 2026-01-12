"""
===========================================================
Array-Based Queue Implementation
===========================================================

Description:
------------
This module provides a basic implementation of a Queue
data structure using Python's built-in list (array).
The queue follows the FIFO (First-In, First-Out) principle.

The implementation is intended for:
    • learning core queue operations
    • understanding FIFO behavior using arrays
    • interview and academic practice

Queue Operations:
-----------------
    • enqueue(val)   : Insert an element at the rear of the queue
    • dequeue()      : Remove and return the front element
    • first()        : Return the front element without removing it
    • is_empty()     : Check whether the queue is empty
    • get_len()      : Return the number of elements in the queue

Exception Handling:
-------------------
    • Raises Empty exception when dequeue() or first() is
      called on an empty queue.

Design Notes:
-------------
    • Internally uses a Python list to store elements.
    • dequeue() uses pop(0), which causes element shifting.

Time Complexity:
----------------
    • enqueue()  : O(1)
    • first()    : O(1)
    • dequeue()  : O(n)  (due to left-shift of elements)

Limitations:
------------
    • Not optimized for large-scale usage.
    • For production systems, collections.deque or a
      circular array implementation is preferred.

Author:
-------
    Thajunniza M A

===========================================================
"""

class Empty(Exception):
    pass
class ArrayQueue:
    def __init__(self):
        self.data = []

    def get_len(self):
        return len(self.data)
    
    def is_empty(self):
        return self.get_len() == 0
    
    def first(self):
        if self.is_empty():
            return Empty("Queue is Empty") 
        return self.data[0]
    
    def enqueue(self,val):
        self.data.append(val)
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        self.data.pop(0)
    
    def printQueue(self):
        print(self.data)


# ===========================================================
# Test Results
# ===========================================================
# Example run
Q1 = ArrayQueue()
Q1.enqueue(1)
Q1.enqueue(2)
Q1.printQueue()
Q1.enqueue(3)
Q1.dequeue()
Q1.printQueue()
print(Q1.first())
