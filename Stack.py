""" 
Stack Data Structure
# Crate a class Stack and constructor will initialize
# python list
# class variable that I’m calling items, and I’m assigning it to an empty list. self.items
"""

class Stack:
    def __init__(self):
        self.items = []
# inserts an item    
    def push(self,item):
        self.items.append(item)
# gives the last item and remove it    
    def pop(self):
        return self.items.pop()
# returns all item
    def getStack(self):
        return self.items
# check if the arrayis empty
    def isEmpty(self):
      return self.items == []  
# Returns the last element of the list
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]    

myStack = Stack()
myStack.push(1)
myStack.push(3)
myStack.push(5)
myStack.push(7)
print(myStack.getStack())
print(myStack.pop())
print(myStack.getStack())
print(myStack.isEmpty())
print(myStack.peek())