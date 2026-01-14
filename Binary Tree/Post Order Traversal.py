"""
===========================================================
Post-order Traversal
===========================================================
Postorder Traversal is a method to traverse a tree such that 
for each node, you first traverse its left subtree,then 
traverse its right subtree and finally visit the node itself.

Pattern :  Left, Right, Root.

Steps:
1.  Check if the current node is empty/null.
2.  Traverse the left subtree by recursively calling the post-order method.
3.  Traverse the right subtree by recursively calling the post-order method.
4.  Display the data part of the root (or current node).
"""
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        print(root.val,end="->")

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

    postorder(BT.root)



