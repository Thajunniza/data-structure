""" 
Linked List always have 4 patters
Basic Node
For travesring as this code- “Start from head, move until None.”
curr = head
while curr:
curr = curr.next
Pattern 1 - Dummy Node Pattern 

"""


## Always a basic node structure
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

## For traver
    