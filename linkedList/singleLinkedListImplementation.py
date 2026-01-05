"""
===========================================================
SINGLE LINKED LIST IMPLEMENTATION
===========================================================
It is a Linear Data Structure where elements is not stored 
in the contiguous memory but each node has two components
    1 . Value
    2 . Pointer to the next Node
With the Pointer information you can traverse to the LL
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

Algorithmic / Interview Operations
-----------------------------------------------------------
14. reverse()               -> Reverse the linked list in-place
15. findMiddle()            -> Find the middle node (slow/fast pointer)
16. hasCycle()              -> Detect cycle using Floyd’s algorithm
17. removeNthFromEnd(n)     -> Remove nth node from the end
===========================================================
✅ Python Solution 
===========================================================
"""
# Class to Create a New Node
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

# Class to Implement Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
    
    """ Print the LinkedList
    -----------------------------------------------------------
    Time:  O(n) 
    """
    def print(self):
        curr = self.head
        if not curr:
            print("No Elements in Linked List")
            return
        while curr:
            print(curr.val,end=" -> " if curr.next else "\n")
            curr = curr.next
        
    """ Function to insert an element last
    -----------------------------------------------------------
    Time:  O(n) 
    """
    def append(self,val):
        """append data at end
        Args:
            data (_type_): any val
        inserts ele at end of the linked list
        check if no node in LL. If yes then the new
        node is head.Else travesre till last and
        last.next is new node
        """
        newnode = Node(val)
        if not self.head:
            newnode.next = self.head
            self.head =newnode
            self.len += 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newnode
        self.len += 1
    
    """ Function to insert an element at top
    -----------------------------------------------------------
    Time:  O(1)  
    """
    def prepend(self,val):
        """Push Element at Top
        Args:
            data(__type__): any val
        """
        newnode = Node(val,self.head)
        self.head = newnode
        self.len += 1
    
    """ Function to insert at index
    -----------------------------------------------------------
    Time:  O(n)  
    """
    def insert(self,val,index):
        """Insert value in the mentioned index
        Args:
            data(__type__): any val
            data(__type__): num index
        """
        if index < 0 or index > self.len:
            raise IndexError
        dummy = Node(0,self.head)
        prev = dummy
        for _ in range(index):
            if not prev.next:
                raise IndexError("Index out of range")
            prev = prev.next
        if not prev:
            raise IndexError("Index out of range")
        newnode = Node(val,prev.next)
        prev.next = newnode
        self.head = dummy.next
        self.len += 1
        
    """ Function to get the length of Linked Lisy
    -----------------------------------------------------------
    Time:  O(1)  
    """
    def getLength(self):
        return self.len
    
    """ Function to check is Linked List is empty
    -----------------------------------------------------------
    Time:  O(1)  
    """
    def isEmpty(self):
        return self.len == 0
    
    """ Function to delete first Node
    -----------------------------------------------------------
    Time:  O(1)  
    """
    def pop(self):
        if self.isEmpty():
            print("No Data to delete")
            return
        val = self.head.val
        self.head = self.head.next
        self.len -= 1
        return val
    
    """ Function to delete Last
    -----------------------------------------------------------
    Time:  O(n)  
    """
    def deleteLast(self):
        if self.isEmpty():
            print("No Data to delete")
            return
        curr = self.head
        if not curr.next:
            val = self.head.val
            self.head = None
            self.len -= 1
            return val
        while curr.next.next:
            curr = curr.next
        val = curr.next.val  
        self.len -=1  
        curr.next = None    
        return val
    
    """ Function to delete value
    -----------------------------------------------------------
    Time:  O(n))  
    """
    def delete(self,val):
        if self.isEmpty():
            print("No Data")
            return None
        dummy = Node(0,self.head)
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
                self.len -= 1
                self.head = dummy.next
                return val
            prev = prev.next
        self.head = dummy.next
        return None
    
    """ Function to delete value by index
    -----------------------------------------------------------
    Time:  O(n)  
    """
    def deleteAtIndex(self,indx):
        if indx < 0 or indx >= self.len:
            print("No Data")
            return None
        dummy = Node(0,self.head)
        prev = dummy
        for _ in range(indx):
            prev = prev.next
        val = prev.next.val
        prev.next = prev.next.next
        self.len -= 1
        self.head = dummy.next
        return val
    
    """ Function to get the value by index
    -----------------------------------------------------------
    Time:  O(n)  
    """ 
    def get(self,index):
        if index < 0  or index >= self.len:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
    
    """ Function to set the value by index
    -----------------------------------------------------------
    Time:  O(n)  
    """ 
    def set(self,val,index):  
        if index < 0  or index >= self.len:
            return False
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.val = val
        return True  
    
    """ Function to search a value
    -----------------------------------------------------------
    Time:  O(n)  
    """ 
    def search(self,val):  
        if self.isEmpty():
            return False
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False


# ===========================================================
# Test Results
# ===========================================================
# Example run
if __name__ == "__main__":
    l1 = LinkedList()
    l1.print()
    l1.append(2)
    l1.append(4)
    l1.print()
    l1.append(6)
    l1.append(8)
    l1.print()
    l1.prepend(1)
    print(f"Is Linked is Empty:{l1.isEmpty()}")
    l1.print()
    l1.prepend(3)
    l1.prepend(5)
    l1.print()
    l1.insert(5,6)
    l1.print()
    print(l1.pop())
    l1.print()
    print(l1.deleteLast())
    l1.print()
    print(l1.delete(4))
    l1.print()
    print(l1.delete(7))
    print(f"The Length is: {l1.getLength()}")
    print(l1.deleteAtIndex(7))
    print(f"The Length is: {l1.getLength()}")
    print(l1.deleteAtIndex(2))
    print(l1.print())
    print(l1.get(2))
    print(l1.get(7))
    l1.set(10,1)
    l1.print()
    print(f"The Length is: {l1.getLength()}")
    print(l1.search(10))
    print(l1.search(55))
    l2 = LinkedList()
    print(f"Is Linked is Empty:{l2.isEmpty()}")
    l2.append(2)
    l2.print()
    print(l2.deleteLast())
    l2.print()
    print(f"The Length is: {l2.getLength()}")
    
        
            
            