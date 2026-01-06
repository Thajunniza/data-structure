"""
===========================================================
QUEUE IMPLEMENTATION USING LINKED LIST
===========================================================
The basic properties of Queue is Linear Data Structure where
but if follow FIFO Operation which means element insertion
happens and the end of the queue and deletion happens at the
start of the queue.So what ever came first should be removed
first.Here we represent start as Head and end as Tail
-----------------------------------------------------------
Core Operations
-----------------------------------------------------------
1. __len__()                -> Return the total number of elements
2. is_empty()               -> Check if stack is empty
3. enqueue(value)           -> Add the element at the end
4. first()                  -> Return the top element
5. dequeue()                -> Delete and return first node
-----------------------------------------------------------
Time & Space Complexity
-----------------------------------------------------------
enqueue(value)  -> Time: O(1), Space: O(1)
dequeue()       -> Time: O(1), Space: O(1)
first()         -> Time: O(1), Space: O(1)
is_empty()      -> Time: O(1), Space: O(1)
__len__()       -> Time: O(1), Space: O(1)
printQueue()    -> Time: O(n), Space: O(1)
-----------------------------------------------------------
Overall Space   -> O(n)  (for n elements in Queue)
-----------------------------------------------------------
===========================================================
✅ Python Solution 
====
"""
class Empty(Exception):
    pass

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self,val):
        newNode = Node(val)
        if self.is_empty():
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1
    
    def first(self):
        if self.is_empty():
            raise Empty("The Queue is Empty")
        return self.head.val
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("The Queue is Empty")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return val
    
    def printQueue(self):
        curr = self.head
        print("[",end="")
        while curr:
            print(curr.val,end="," if curr.next else '')
            curr = curr.next
        print("]")

# ===========================================================
# Test Results
# ===========================================================
# Example run
Q1 = LinkedQueue()
Q1.enqueue(1)
Q1.enqueue(2)
Q1.printQueue()
Q1.enqueue(3)
Q1.dequeue()
Q1.printQueue()
print(Q1.first())