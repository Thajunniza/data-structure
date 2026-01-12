"""
===========================================================
Circular Queue Implementation using Array
===========================================================

A Circular Queue is a linear data structure that follows the
FIFO (First-In-First-Out) principle and overcomes the memory
wastage problem of a simple array-based queue by treating the
array as circular.

This implementation uses:
• A fixed-size array
• Two pointers: `first` (front) and `last` (rear)
• Modulo arithmetic for circular indexing

Key Operations:
• enqueue(val)  → Insert an element at the rear
• dequeue()     → Remove and return the front element
• is_empty()    → Check if the queue is empty
• is_full()     → Check if the queue is full
• find_size()   → Get current number of elements
• display()     → Print queue elements in order

Conditions:
• Queue is empty when: first == -1
• Queue is full when: (last + 1) % max_size == first
  (or size == max_size)

Time Complexity:
• Enqueue   → O(1)
• Dequeue   → O(1)
• Peek      → O(1)
• Size      → O(1)

Space Complexity:
• O(n), where n is the maximum size of the queue

Use Cases:
• CPU scheduling
• Buffer management
• Streaming data processing
• Circular task execution

Author: Thajunniza
"""


class Full(Exception):
    pass

class CircularArrayQueue:
    def __init__(self):
        self.max_size = 10
        self.data = [None] * self.max_size
        self.first = -1
        self.last = -1
    
    def find_size(self):
        if self.is_empty():
            return 0
        if self.last >= self.first:
            return self.last - self.first + 1
        return self.max_size - (self.first - self.last - 1)
    
    def is_empty(self):
        return self.first == -1
    
    def is_full(self):
        return self.find_size() == self.max_size
    
    def enqueue(self, val):
        if self.is_full():
            raise Full("Queue is Full")
        
        if self.is_empty():
            self.first = 0
            self.last = 0
        else:
            self.last = (self.last + 1) % self.max_size
        
        self.data[self.last] = val
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        
        val = self.data[self.first]
        
        if self.first == self.last:
            self.first = -1
            self.last = -1
        else:
            self.first = (self.first + 1) % self.max_size
        
        return val
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        i = self.first
        while True:
            print(self.data[i], end=" ")
            if i == self.last:
                break
            i = (i + 1) % self.max_size
        print()


cq = CircularArrayQueue()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()     # 10 20 30 40

print(cq.dequeue())  # 10
cq.enqueue(50)
cq.enqueue(60)

cq.display()     # 20 30 40 50 60



        