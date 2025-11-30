""" 
Stack Data Structure
"""

class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def getStack(self):
        return self.items
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    

myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.getStack())
myStack.push("C")
print(myStack.getStack())
myStack.pop()
print(myStack.getStack())
print(myStack.is_empty())
print(myStack.peek())