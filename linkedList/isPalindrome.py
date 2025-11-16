"""
## Is Palindrome
determine if a singly linked list is a palindrome,
that is if the data held at each of the nodes in the linked list
can be read forward from the head or backward from the tail to generate the same content. 
## what a palindrome 
# A palindrome is a word or a sequence that is the same from the front as from the back.
# For instance, racecar and radar are palindromes.
# Examples of non-palindromes are ABC, hello, and test.

## Solution 1: Using a string
Move the linked list to string and reverse a string then check both

## Solution 2: Using stack
push the list to stack using append
then pop and check the Linked list

## Solution 3: Using Two Pointers
two pointers p and q.
p will initially point to the head of the list and q to the last node of the list. 
see if p and q are equal if not return false
if yes move forward 
return when p and q meet
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
    def is_palindrome(self,sol):
        if sol == 1:
            curr = self.head
            str = ""
            while curr:
                str += curr.data
                curr = curr.next
            revStr = str[::-1]
            return str == revStr
        if sol == 2:
            curr = self.head
            s = []
            while curr:
                s.append(curr.data)
                curr = curr.next
            curr = self.head
            while curr:
                data = s.pop()
                if curr.data != data:
                    return False
                curr = curr.next
            return True
        if sol == 3:
            s = []
            p = self.head
            q = self.head
            i = 0
            while q:
                s.append(q)
                q = q.next
                i += 1
            q = s[i-1]
            count = 1
            while count <= i//2 + 1:
                if s[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True
                    
      
    
    
             
# Example palindromes:
# RACECAR, RADAR

# Example non-palindromes:
# TEST, ABC, HELLO

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("C")
llist.append("E")
llist.append("C")
llist.append("A")
llist.append("R")
print(llist.is_palindrome(1))
print(llist.is_palindrome(2))
print(llist.is_palindrome(3))
llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")
print(llist_2.is_palindrome(1))
print(llist_2.is_palindrome(2))
print(llist_2.is_palindrome(3))