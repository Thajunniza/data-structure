"""
Linked List always have 
Basic Node
For travesring as this code- “Start from head, move until None.”
curr = head
while curr:
curr = curr.next

"""


## Always a basic node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------- Helper Functions ----------


def buildLinkedList(arr):
    """Build a linked list from a Python list and return the head node.

    Example:
        head = build_list([1, 2, 3])
        # head -> 1 -> 2 -> 3 -> None
    """
    dummy = ListNode()
    curr = dummy
    for n in arr:
        newNode = ListNode(n)
        curr.next = newNode
        curr = curr.next
    return dummy.next

def print_list(head):
    """Print the linked list in a readable format.

    Example:
        1 -> 2 -> 3 -> None
    """
    curr = head
    while(curr):
        print(curr.val,end="->")
        curr = curr.next
    print("None")

head = buildLinkedList([1,2,3,4,5])
print_list(head)
