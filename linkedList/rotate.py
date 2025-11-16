"""
Rotate
rotate the nodes of a singly linked list around a specified pivot element.
shifting or rotating everything that follows the pivot node to the front of the linked list.

1->2->3->4->5
if ivot = 3
4->5->1->2->3
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
    
    def rotate(self, k):
        if not self.head:
            return
        curr = self.head
        prev = None
        p = None
        q = None
        i = 0
        while curr:
            i += 1
            if (i == k):
                p = curr
                q = curr
            prev = curr
            curr = curr.next   
        if not p or not q:
            return
        prev.next =self.head
        self.head = p.next
        p.next = None 
        
    
## Execution
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.rotate(3)
llist.print_list()
    
    
             
