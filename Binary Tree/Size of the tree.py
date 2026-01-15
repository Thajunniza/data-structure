"""
===========================================================
Size of a Binary Tree
===========================================================

Tree Size can be defined by counting the total no of nodes
1. Using Recursion
2. Using Stack

Note:
- All methods visit every node → Time Complexity = O(n)
- Recursive approach uses call-stack space
- Queue (BFS) approach uses auxiliary space
"""

from collections import deque


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


# ---------------------------------------------------------
# Size using Recursion (DFS)
# ---------------------------------------------------------
def size_recur(root):
    """
    Returns size of tree m.
    Empty tree  ->0
    Single node -> 1
    """
    if not root:
        return 0

    left_size = size_recur(root.left)
    right_size = size_recur(root.right)

    return 1 + left_size + right_size


# ---------------------------------------------------------
# Size using Stack (DFS)
# ---------------------------------------------------------
def size_stack(root):
    """
    Returns size of tree m.
    Empty tree  ->0
    Single node -> 1
    """
    if not root:
        return 0

    stack = []
    stack.append(root)
    size = 1
    while stack:
        node = stack.pop()
        if node.left:
            size += 1
            stack.append(node.left)
        if node.right:
            size += 1
            stack.append(node.right)
    return size


# ---------------------------------------------------------
# Driver Code
# ---------------------------------------------------------
if __name__ == "__main__":

    # Binary Tree Structure
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

    print("Size - Recursive :", size_recur(BT.root))
    print("Size - Stack :", size_stack(BT.root))
