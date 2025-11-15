"""
Linked List
# Every linked list consists of nodes,Every node has two components:
# Data - store an element of data
# Next - a pointer that points from one node to another.
# Now let’s go ahead and create our classes in Python:
# Node class
# LinkedList class
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


""" 
# INSERTION
## append - insert an element at the end of the linked list. 
## prepend -  insert an element at the beginning of the linked list
## insert_after_node -  inserting an element after a given node.
"""


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

    def prepend(self, data):
        """
        insert an element at the beginning of the linked list
        head should be the new data
        and new data next should point to head
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

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

    def delete_node(self, key):
        """
        Deletion
        to delete a node, we’ll first find the node to be deleted by traversing the linked list.
        Then, we’ll delete that node and update the rest of the pointers.
        To solve this problem, we need to handle two cases:
        Node to be deleted is head.
        Node to be deleted is not head.
        """
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        else:
            prev = None
            while curr_node and curr_node.data != key:
                prev = curr_node
                curr_node = curr_node.next

            if curr_node is None:
                return

            prev.next = curr_node.next
            curr_node = None

    def delete_node_at_pos(self, pos):
        curr_node = self.head
        if pos == 0:
            curr_node = self.head
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        i = 0
        while i != pos and curr_node:
            prev = curr_node
            curr_node = prev.next
            i += 1
        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def len_iterative(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node):
        count = 0
        if node == None:
            return count
        else:
            count = 1 + self.len_recursive(node.next)
            return count

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        if self.head == None:
            return
        if self.head.next == None:
            return
        prev1 = None
        curr1 = self.head
        prev2 = None
        curr2 = self.head

        while curr1 and curr1.data != key_1:
            prev1 = curr1
            curr1 = curr1.next

        while curr2 and curr2.data != key_2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):
        if self.head == None:
            return
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if cur is None:
                return prev
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            return _reverse_recursive(cur, prev)

        self.head =  _reverse_recursive(self.head, prev=None)


## Execution
llist = LinkedList()
# Append
llist.append("A")
llist.append("B")
llist.print_list()
print("*******")
llist.append("C")
llist.append("D")
llist.print_list()
print("*******")
# Prepend
llist.prepend("D")
llist.print_list()
### Insert
print("*******")
llist.insert_after_node(llist.head.next, "D")
llist.print_list()
## Delete
print("*******")
llist.delete_node("B")
llist.delete_node("E")
llist.print_list()

## Delete by position
print("*******")
llist.delete_node_at_pos(1)
llist.print_list()

##Length of Linked List
print("*******")
print("Length of Linked List")
print(llist.len_iterative())

##Length of Linked List by Recursion
print("*******")
print("Length of Linked List")
print(llist.len_recursive(llist.head))
## Swap Nodes
print("*******")
llist.swap_nodes("D", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()
## Reverse
print("*******")
llist.reverse_iterative()
llist.print_list()
## Reverse Using Recurrsion
print("*******")
llist.reverse_recursive()
llist.print_list()

