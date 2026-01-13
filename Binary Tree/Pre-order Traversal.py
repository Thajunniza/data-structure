"""
===========================================================
Pre-order Traversal
===========================================================
Preorder Traversal is a method to traverse a tree such that 
for each node, you first visit the node itself, then traverse
its left subtree, and finally traverse its right subtree. 

Pattern :  Root, Left, Right.

Steps:
1. Check if the current node is empty/null.
2. Display the data part of the root (or current node).
3. Traverse the left subtree by recursively calling the pre-order method.
4. Traverse the right subtree by recursively calling the pre-order method.
"""
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


def preorder(root):
        if not root:
            return
        print(root.val,end="->")
        preorder(root.left)
        preorder(root.right)

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

    preorder(BT.root)



