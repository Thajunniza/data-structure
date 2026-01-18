"""
===========================================================
Total Sum of a Binary Tree
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
# Sum using Recursion (DFS)
# ---------------------------------------------------------
def sum_recur(root):
    """
    Returns size of tree m.
    Empty tree  ->0
    Single node -> 1
    """
    if not root:
        return 0
    
    leftval = sum_recur(root.left)
    rightval = sum_recur(root.right)
    
    return root.val + leftval + rightval


# ---------------------------------------------------------
# Sum using Stack (DFS)
# ---------------------------------------------------------
def sum_stack(root):
    """
    Returns size of tree m.
    Empty tree  ->0
    Single node -> 1
    """
    if not root:
        return 0

    stack = []
    stack.append(root)
    result = 0
    while stack:
        node = stack.pop()
        result += node.val
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result


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

    print("Sum - Recursive :", sum_recur(BT.root))
    print("Sum - Stack :", sum_stack(BT.root))
