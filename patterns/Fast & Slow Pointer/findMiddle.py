"""
We need to find the middle of the list using fast and slow
if length / 2 + 1 th element
if list has 5 nodes then its 3rd node
1 -> 2 -> 3 -> 4 -> 5 -> None
Middle is: 3
For even-length lists, fast & slow pointer ALWAYS return the second middle.
if list has 6 nodes then its
1 → 2 → 3 → 4 → 5 → 6
Middle is 4
"""


class LinkeNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Helper functions
def buildLinkedList(arr):
    dummy = LinkeNode()
    curr = dummy
    for n in arr:
        newNode = LinkeNode(n)
        curr.next = newNode
        curr = curr.next
    return dummy.next


def printList(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("None")

def findMiddle(head): 
    p = head
    q = head
    while q and q.next:
        p = p.next 
        q = q.next.next   
    return p

## Execution
head = buildLinkedList([1, 2, 3, 4, 5])
printList(head)
print(findMiddle(head).val)
head = buildLinkedList([1, 2, 3, 4, 5,6])
printList(head)
print(findMiddle(head).val)

""" 
## Output 
1->2->3->4->5->None
3
1->2->3->4->5->6->None
4
"""