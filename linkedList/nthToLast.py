""" 
## Nth-to-Last Node
if N equals 2, we want to get the second to last node from the linked list.
## Solution 1
We’ll break down this solution in two simple steps:

Calculate the length of the linked list.
Count down from the total length until n is reached.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """append the data at end of list
        Args:
            data (_type_): any data
        first creat a node for the data
        then check if linked list is empty
        if empty mark the head as the new node
        else
        get the last node by traversing from head
        """
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    def print_list(self):
        """
        print out the entries of a linked list.
        start from head if head is not empty
        print head and map ton next
        """
        curr_data = self.head
        while curr_data:
            print(curr_data.data)
            curr_data = curr_data.next
    
    def getLength(self):
        i = 0
        curr = self.head
        while curr:
            i += 1
            curr = curr.next
        return i
    
    def print_nth_from_last(self, n, method):
        if method == 1:
            len = self.getLength()
            if len == 0 or len < n:
                return
            i = len -n
            curr = self.head
            while i > 0:
                i -= 1
                curr = curr.next
            return curr.data
        else:
            p = self.head
            q = self.head
            if not p or n == 0:
                return None
            i = 1
            while q and i < n:
                i += 1
                q = q.next
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return
            while q.next:
                p = p.next
                q = q.next
            return p.data
            
    

## Execution
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.print_nth_from_last(4,1))
print(llist.print_nth_from_last(4,2))
print(llist.print_nth_from_last(2,1))
print(llist.print_nth_from_last(2,2))