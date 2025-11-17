"""
# Find Start of Cycle
# 1 → 2 → 3 → 4 → 5
#         ↑       ↓
#         ← ← ← ←

# when the slow and fast meet that is not start of the Cycle
# it just confirm the linked list is a Cycle
# to get the start of the cycle

# Steps:
# 1. First, detect if there is a cycle (same as above).
# 2. Suppose slow & fast meet at node 4 (inside cycle).
# 3. Now:
# Move slow back to head
# Keep fast at meeting point
# Move both 1 step at a time:

# slow: 1 → 2 → 3

# fast: 4 → 5 → 3

# They meet at node 3 → this is the cycle start.
"""


class LinkeListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Helper function to build a list
def buildLinkedList(arr):
    dummy = LinkeListNode()
    curr = dummy
    for n in arr:
        newNode = LinkeListNode(n)
        curr.next = newNode
        curr = curr.next
    return dummy.next


## Helper function to display the Linked List
def printList(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print(None)


def detectCycleStart(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


## Execution
head = buildLinkedList([1, 2, 3, 4, 5])
printList(head)
# Get references to each node
n1 = head  # value = 1
n2 = n1.next  # value = 2
n3 = n2.next  # value = 3
n4 = n3.next  # value = 4
n5 = n4.next  # value = 5

# Create cycle: node 5 points to node 3
n5.next = n3
print(detectCycleStart(head).val)
