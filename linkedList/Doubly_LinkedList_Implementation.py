"""
===========================================================
DOUBLE LINKED LIST IMPLEMENTATION
===========================================================
It is special kind of LinkedList where the node can navigate
in both directions as each node contains a pointer to the 
previous node as well as the next node of linked list.
-----------------------------------------------------------
Core Operations
-----------------------------------------------------------
1. append(value)            -> Insert node at the end
2. prepend(value)           -> Insert node at the beginning
3. insert(value, index)     -> Insert node at a specific index
4. pop()                    -> Delete and return first node
5. deleteLast()             -> Delete and return last node
6. delete(value)            -> Delete first occurrence of value
7. deleteAtIndex(index)     -> Delete node at a specific index

Access & Utility Operations
-----------------------------------------------------------
8. get(index)               -> Get value at a specific index
9. set(index, value)        -> Update value at a specific index
10. search(value)           -> Check if value exists in the list
11. getLength()             -> Return total number of nodes
12. isEmpty()               -> Check if the list is empty
13. display() / printList() -> Traverse and print the list

===========================================================
✅ Python Solution 
===========================================================
"""
class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get_length(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val,end=" -> " if curr.next else "\n")
            curr = curr.next
    
    
    # --------------------------
    # Insertion operations
    # --------------------------
    # Insert element at Last
    def append(self,val):
        newNode = Node(val)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
    
    # Insert Element at first
    def prepend(self,val):
        newNode = Node(val,None,self.head)
        if self.is_empty():
            self.tail = newNode
        self.head.prev = newNode
        self.head = newNode
        self.size += 1
    
    # Insert at Index
    def insert(self,val,index):
        if index < 0 or index > self.size:
            raise IndexError("Invalid Index")
        if index == 0:
            self.prepend(val)
            return
        if index == self.size:
            self.append(val)
            return
        curr = self._get_node_atIndex(index)
        prev = curr.prev
        newNode = Node(val,prev,curr)
        prev.next = newNode
        curr.prev = newNode 
        self.size += 1   
    
    # --------------------------
    # Removal operations
    # --------------------------
    def delete_first(self):
        if self.is_empty():
            raise IndexError("Delete from Expty List")
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
    
    def delete_last(self):
        if self.is_empty():
            raise IndexError("Delete from Empty List")
        self.size -= 1
        self.tail.prev.next = None
        if self.is_empty():
            self.head = None
    
    def delete_byIndex(self,index):
        if self.is_empty():
            raise IndexError("Delete from Empty List")
        curr = self._get_node_atIndex(index)
        if not curr:
            raise IndexError("Index out of Range")
        if index == 0:
            self.delete_first()
            return
        if index == self.size-1:
            self.delete_last()
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.size -= 1
        

    def _get_node_atIndex(self,index):
        if index < 0 and index >= self.size:
            return None
        # Bidirectional Walk
        if index <= self.size//2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev
            return curr
        
    def clear(self):
        curr = self.head
        while curr:
            nxt = curr.next
            curr.prev = None
            curr.next = None
            curr  = nxt
        self.head = self.tail = None
        self.size = 0

# ===========================================================
# Test Results
# ===========================================================
# Example run
if __name__ == "__main__":
    d1 = DoublyLinkedList()       
    d1.print_list()
    d1.append(1)
    d1.append(2)
    d1.print_list()
    d1.prepend(3)
    d1.prepend(4)
    d1.print_list()
    d1.insert(5,1)
    print(d1.get_length())
    d1.print_list()
    d1.delete_first()
    d1.print_list()
    d1.delete_last()
    d1.print_list()
    d1.delete_byIndex(1)
    d1.print_list()
    d1.clear()
    print(d1.get_length())
            
