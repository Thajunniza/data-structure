"""
===========================================================
Height of a Binary Tree
===========================================================

Tree height can be defined in TWO valid ways:

1. Height in EDGES (Algorithm / Interview standard)
   - Height of empty tree  = -1
   - Height of single node = 0

2. Height in NODES (Textbook / Level count)
   - Height of empty tree  = 0
   - Height of single node = 1

Both definitions are correct.
The key requirement is to be explicit and consistent.

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
# Height using Recursion (DFS)
# Definition: Height in EDGES
# ---------------------------------------------------------
def heightRecurEdges(root):
    """
    Returns height of tree measured in EDGES.
    Empty tree  -> -1
    Single node -> 0
    """
    if not root:
        return -1

    left_height = heightRecurEdges(root.left)
    right_height = heightRecurEdges(root.right)

    return 1 + max(left_height, right_height)


# ---------------------------------------------------------
# Height using Recursion (DFS)
# Definition: Height in NODES
# ---------------------------------------------------------
def heightRecurNodes(root):
    """
    Returns height of tree measured in NODES.
    Empty tree  -> 0
    Single node -> 1
    """
    if not root:
        return 0

    return 1 + max(heightRecurNodes(root.left),
                   heightRecurNodes(root.right))


# ---------------------------------------------------------
# Height using Queue (BFS)
# Definition: Height in EDGES
# ---------------------------------------------------------
def heightQueueEdges(root):
    """
    BFS-based height calculation in EDGES.
    """
    if not root:
        return -1

    q = deque([root])
    height = -1

    while q:
        height += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return height


# ---------------------------------------------------------
# Height using Queue (BFS)
# Definition: Height in NODES
# ---------------------------------------------------------
def heightQueueNodes(root):
    """
    BFS-based height calculation in NODES.
    """
    if not root:
        return 0

    q = deque([root])
    height = 0

    while q:
        height += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return height


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

    print("Height (Edges) - Recursive :", heightRecurEdges(BT.root))
    print("Height (Nodes) - Recursive :", heightRecurNodes(BT.root))

    print("Height (Edges) - Queue     :", heightQueueEdges(BT.root))
    print("Height (Nodes) - Queue     :", heightQueueNodes(BT.root))
