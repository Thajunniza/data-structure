"""
===========================================================
Binar Tree Implementation
===========================================================
A binary tree is a tree data structure in which each node
has at most two children, which are referred to as the 
left child and the right child. 
"""
# Define Node for the tree each node has three values stored:
# 1. value - data
# 2.left - Left Node
# 3.right - Right Node

class Node(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


# Test case
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree)