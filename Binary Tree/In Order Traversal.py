"""
===========================================================
In-Order Traversal
===========================================================
InOrder Traversal is a method to traverse a tree such that 
for each node, you first traverse the left subtree itself, then 
visit the node, and finally traverse its right subtree. 

Pattern :  Left, Root , Right.

Steps:
1. Check if the current node is empty/null.
2. Traverse the left subtree by recursively calling the in-order method.
3. Display the data part of the root (or current node).
4. Traverse the right subtree by recursively calling the in-order method.
"""
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val,end="->")
    inorder(root.right)

def inorder_array(root,arr=[]):
    if not root:
        return 
    inorder_array(root.left,arr)
    arr.append(root.val)
    inorder_array(root.right,arr)
    return arr

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

    inorder(BT.root)
    print()
    print(inorder_array(BT.root))

    # 4->5->2->6->3->1->



