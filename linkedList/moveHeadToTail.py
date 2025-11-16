"""
Move Tail to Head
move the tail (or last) node in a singly linked list
to the front of the linked list so that it becomes the new head of the linked list.

A -> B -> C -> D
D -> B -> C -> A
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


    def move_tail_to_head(self):
        p = self.head
        q = self.head
        prev = None
        curr = self.head

        while q.next:
            prev = q
            q = q.next

        prev.next = None
        q.next = p
        self.head = q


## Execution
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.print_list()
print("******")
llist.move_tail_to_head()
llist.print_list()
