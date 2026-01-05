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
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n)  
Space: O(n)

===========================================================
✅ Python Solution 
===========================================================
"""
# Class to Create a New Node
class Node:
    def __init__(self,val,head=None):
        self.val = val
        self.next = head

# Class to Implement Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    """ Print the LinkedList
    -----------------------------------------------------------
    Time:  O(n)  
    Space: O(n)
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
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newnode
    
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
        if not self.head:
            raise IndexError("Index out of range")
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
        
    """ Function to get the length of Linked Lisy
    -----------------------------------------------------------
    Time:  O(n)  
    """
    def getLength(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
        

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
    l1.print()
    l1.prepend(3)
    l1.prepend(5)
    l1.print()
    l1.insert(5,6)
    l1.print()
    print(f"The Length is: {l1.getLength()}")
    l2 = LinkedList()
    l2.append(2)
    l2.print()
    l2.insert(1,0)
    l2.print()
    print(f"The Length is: {l2.getLength()}")
    
        
            
            