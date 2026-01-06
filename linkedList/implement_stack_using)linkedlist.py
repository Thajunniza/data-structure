"""
===========================================================
STACK IMPLEMENTATION USING LINKED LIST
===========================================================
The basic properties of Stack is Linear Data Structure where
the insertion and deletion of element happens only at the
top of stack as it follow LIFO which is Last In First Out
With the help of Linked List we will write functions which
implements Stack Operations
-----------------------------------------------------------
Core Operations
-----------------------------------------------------------
1. __len__()                -> Return the total number of elements
2. is_empty()               -> Check if stack is empty
3. push(value)              -> Add the element at the top
4. top()                    -> Return the top element
5. pop()                    -> Delete and return first node
-----------------------------------------------------------
Time & Space Complexity
-----------------------------------------------------------
push(value)     -> Time: O(1), Space: O(1)
pop()           -> Time: O(1), Space: O(1)
top()           -> Time: O(1), Space: O(1)
is_empty()      -> Time: O(1), Space: O(1)
__len__()       -> Time: O(1), Space: O(1)
printStack()    -> Time: O(n), Space: O(1)
-----------------------------------------------------------
Overall Space   -> O(n)  (for n elements in stack)
-----------------------------------------------------------
===========================================================
✅ Python Solution 
===========================================================
"""
class Empty(Exception):
    pass

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self,val):
        newNode = Node(val,self.head)
        self.head = newNode
        self.size += 1
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self.head.val
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val
    
    def printStack(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        curr = self.head
        print("[",end="")
        while curr:
            print(curr.val,end =',' if curr.next else']\n')
            curr = curr.next
            
            
    
# ===========================================================
# Test Results
# ===========================================================
# Example run

s1 = LinkedStack()
s1.printStack()
s1.push(1)
s1.push(2)
s1.printStack()
s1.push(3)
s1.printStack()
s1.pop()
s1.printStack()
s1.pop()
s1.pop()
s1.printStack()
s1.pop()