""" 
## Merge Two Sorted Linked Lists

# Given two already sorted linked lists,
# make them into one linked list while keeping the final linked list sorted as well

## Algorithm
- We will use 2 pointers p and q which points to the each linked list head
- s will compare p and q and point to the smaller value
- if point to p the p moves forward else q moves forwars
- s is the final linked list

## Solution 
- Step 1: Initialize pointers
- Step 2: Handle empty list edge cases
- Step 3: Pick the FIRST node of the merged list
- Step 4: Merge remaining nodes
- Step 5: Attach the leftover nodes
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
            
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p.data < q.data:
            s = p
            p = s.next
        else:
            s= q
            q = s.next
        new_head = s
        
        while p and q:
            if(p.data < q.data):
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = p
        if not q:
            s.next = q
        self.head = new_head
        return self.head
    

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)
print("List 1")
llist_1.print_list()
llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)
print("List 2")
llist_2.print_list()
print("Merged Sorted List")
llist_1.merge_sorted(llist_2)
llist_1.print_list()
                