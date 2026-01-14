
"""
===========================================================
Reversal Level Order Traversal (Breadth-First Search)
===========================================================
Level order traversal visits nodes level-by-level from left
to right but starting from child using a FIFO queue.

Steps:
1. If the root is None, return an empty result.
2. Initialize a queue and enqueue the root.
3. While the queue is not empty:
   a. Dequeue the front node.
   b. Append its value to the result.
   c. Enqueue its right child if it exists.
   d. Enqueue its left child if it exists.
"""


from collections import deque
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


def reverselevelorder(root):
    if not root:
        return []
    q = deque()
    q.append(root)
    stack = []
    while(q):
        node = q.popleft()
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
        stack.append(node.val)
    while stack:
        print(stack.pop(),end="->")


def reverselevelorderbyGroup(root):
    if not root:
        return []
    result = []
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        group = []
        for _ in range(n):
            node = q.popleft()
            group.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(group)
    return result[::-1]

    
    

if __name__ == "__main__":
    
    # Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
    
    BT = BinaryTree(1)
    BT.root.left = Node(2)
    BT.root.right = Node(3)
    BT.root.left.left = Node(4)
    BT.root.left.right = Node(5)
    BT.root.right.right = Node(6)

    print(reverselevelorder(BT.root))
# 4->5->6->2->3->1->None
# [[4, 5, 6], [2, 3], [1]]



