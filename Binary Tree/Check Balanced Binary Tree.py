"""
===========================================================
Check if a Binary Tree is Height-Balanced
===========================================================

A binary tree is height-balanced if:
For every node,
|height(left subtree) - height(right subtree)| <= 1

Approach:
- Bottom-up DFS
- Return height if balanced
- Return -1 as a sentinel if unbalanced

Time Complexity: O(n)
Space Complexity: O(h)  -> recursion call-stack
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root


# ---------------------------------------------------------
# Check Balanced Binary Tree (Optimized DFS)
# ---------------------------------------------------------
def is_balanced(root):
    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        if left_h == -1:
            return -1

        right_h = height(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return 1 + max(left_h, right_h)

    return height(root) != -1


# ---------------------------------------------------------
# Driver Code
# ---------------------------------------------------------
if __name__ == "__main__":

    # Balanced Tree
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    BT1 = BinaryTree(root1)
    print("Is Balanced (Tree 1):", is_balanced(BT1.root))

    # Unbalanced Tree
    #       1
    #      /
    #     2
    #    /
    #   3
    root2 = Node(1)
    root2.left = Node(2)
    root2.left.left = Node(3)

    BT2 = BinaryTree(root2)
    print("Is Balanced (Tree 2):", is_balanced(BT2.root))
