""" 
Detect if a Linked List has a Cycle
list with a cycle:
1 → 2 → 3 → 4 → 5
        ↑       ↓
        ← ← ← ←
How to detect
At some point, fast runs inside the cycle and “chases” slow.

Because fast moves 2 steps and slow 1 step, they will eventually meet if there's a cycle.
Steps:
1. First, detect if there is a cycle (same as above).
2. Suppose slow & fast meet at node 4 (inside cycle).
"""

class LinkedListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next
        
## Helper Class to build the list 
def buildLinkedList(arr):
    dummy = LinkedListNode()
    curr = dummy
    for n in arr:
        newNode = LinkedListNode(n)
        curr.next = newNode
        curr = curr.next
    return dummy.next

## Helper class to print the list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next 
        
    print(None)

## check if linked list in cycle
def isCycle(head):
    p = head
    q = head
    
    while q and q.next:
        p = p.next
        q = q.next.next
        
        if p == q: 
            return True
    return False
    
    
    
## Execution
head = buildLinkedList([1,2,3,4,5])
printList(head)
print(isCycle(head))
# Get references to each node
n1 = head            # value = 1
n2 = n1.next         # value = 2
n3 = n2.next         # value = 3
n4 = n3.next         # value = 4
n5 = n4.next         # value = 5

# Create cycle: node 5 points to node 3
n5.next = n3
print(isCycle(head)) 
