"""
===========================================================
Binary Tree Traversal & Property Validation – Test Suite
===========================================================

Purpose:
--------
This test suite validates the correctness of binary tree
traversals and structural property computations implemented
in the Solution class.

Covered Scenarios:
------------------
1. Complete Binary Tree
2. Sparse Binary Tree (with None gaps)
3. Single Node Tree
4. Empty Tree

Validated Operations:
---------------------
- Inorder Traversal (Recursive & Iterative)
- Preorder Traversal (Recursive & Iterative)
- Postorder Traversal (Recursive & Iterative)
- Level Order Traversal (BFS)
- Tree Height (Recursive & BFS)
- Tree Size (Recursive & Iterative)
- Reverse Level(Iterative)


Time Complexity:
----------------
Each traversal or property computation runs in O(n),
where n is the number of nodes in the tree.

Space Complexity:
-----------------
- DFS-based methods: O(h), where h is tree height
- BFS-based methods: O(w), where w is max tree width
"""


from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level):
    """
    Build binary tree from level-order list.
    Time: O(n)
    Space: O(n)
    """
    if not level or level[0] is None:
        return None

    root = Node(level[0])
    q = deque([root])
    i = 1

    while q and i < len(level):
        node = q.popleft()

        # Left child
        if i < len(level) and level[i] is not None:
            node.left = Node(level[i])
            q.append(node.left)
        i += 1

        # Right child
        if i < len(level) and level[i] is not None:
            node.right = Node(level[i])
            q.append(node.right)
        i += 1

    return root


class Solution:
    # =========================
    # INORDER TRAVERSAL
    # =========================

    def inorder1(self, root):
        """
        Recursive inorder
        Time: O(n)
        Space: O(h)
        """
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

    def inorder2(self, root):
        """
        Iterative inorder
        Time: O(n)
        Space: O(h)
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

    # =========================
    # PREORDER TRAVERSAL
    # =========================

    def preorder1(self, root):
        """
        Recursive preorder
        Time: O(n)
        Space: O(h)
        """
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

    def preorder2(self, root):
        """
        Iterative preorder
        Time: O(n)
        Space: O(h)
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    # =========================
    # POSTORDER TRAVERSAL
    # =========================

    def postorder1(self, root):
        """
        Recursive postorder
        Time: O(n)
        Space: O(h)
        """
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result

    def postorder2(self, root):
        """
        Iterative postorder (single stack with visited flag)
        Time: O(n)
        Space: O(h)
        """
        if not root:  # FIX: null guard added
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return result

    # =========================
    # BFS / LEVEL ORDER
    # =========================

    def bfs(self, root):
        """
        Level order traversal
        Time: O(n)
        Space: O(w)
        """
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            node = q.popleft()
            result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return result

    # =========================
    # HEIGHT OF TREE
    # =========================

    def height1(self, root):
        """
        Recursive height (node-based)
        Time: O(n)
        Space: O(h)
        """
        if not root:
            return 0
        return 1 + max(self.height1(root.left), self.height1(root.right))

    def height2(self, root):
        """
        Iterative height using BFS
        Time: O(n)
        Space: O(w)
        """
        if not root:
            return 0

        height = 0
        q = deque([root])

        while q:
            level_size = len(q)
            height += 1

            for _ in range(level_size):
                node = q.popleft()  # FIX: popleft (queue semantics)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return height  # FIX: removed -1

    # =========================
    # SIZE OF TREE
    # =========================

    def size1(self, root):
        """
        Recursive size
        Time: O(n)
        Space: O(h)
        """
        if not root:
            return 0
        return 1 + self.size1(root.left) + self.size1(root.right)

    def size2(self, root):
        """
        Iterative size
        Time: O(n)
        Space: O(h)
        """
        if not root:
            return 0

        count = 0
        stack = [root]

        while stack:
            node = stack.pop()
            count += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return count
    
    # =========================
    # REVERSE LEVEL ORDER
    # =========================

    def reverse_level(self, root):
        """
        Level order traversal
        Time: O(n)
        Space: O(w)
        """
        if not root:
            return []

        result = []
        q = deque([root])
        stack = []

        while q:
            node = q.popleft()
            stack.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        while stack:
            result.append(stack.pop())

        return result


# =========================
# TEST CASE 1: Complete Binary Tree
# =========================

root = build_tree([1, 2, 3, 4, 5, 6])
sol = Solution()

print("=== Test Case 1: Complete Binary Tree ===")
print("Inorder (rec)   :", sol.inorder1(root))
print("Inorder (iter)  :", sol.inorder2(root))
print("Preorder (rec) :", sol.preorder1(root))
print("Preorder (iter):", sol.preorder2(root))
print("Postorder (rec):", sol.postorder1(root))
print("Postorder (iter):", sol.postorder2(root))
print("Level Order    :", sol.bfs(root))
print("Height (rec)   :", sol.height1(root))
print("Height (iter)  :", sol.height2(root))
print("Size (rec)     :", sol.size1(root))
print("Size (iter)    :", sol.size2(root))
print("Reverse (iter)    :", sol.reverse_level(root))
print()


# =========================
# TEST CASE 2: Sparse Binary Tree
# =========================

root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

print("=== Test Case 2: Sparse Binary Tree ===")
print("Inorder (rec)   :", sol.inorder1(root))
print("Inorder (iter)  :", sol.inorder2(root))
print("Preorder (rec) :", sol.preorder1(root))
print("Preorder (iter):", sol.preorder2(root))
print("Postorder (rec):", sol.postorder1(root))
print("Postorder (iter):", sol.postorder2(root))
print("Level Order    :", sol.bfs(root))
print("Height (rec)   :", sol.height1(root))
print("Height (iter)  :", sol.height2(root))
print("Size (rec)     :", sol.size1(root))
print("Size (iter)    :", sol.size2(root))
print("Reverse (iter)    :", sol.reverse_level(root))
print()


# =========================
# TEST CASE 3: Single Node Tree
# =========================

root = build_tree([1])

print("=== Test Case 3: Single Node Tree ===")
print("Inorder        :", sol.inorder1(root))
print("Preorder       :", sol.preorder1(root))
print("Postorder      :", sol.postorder1(root))
print("Level Order    :", sol.bfs(root))
print("Height         :", sol.height1(root))
print("Size           :", sol.size1(root))
print("Reverse (iter)    :", sol.reverse_level(root))
print()


# =========================
# TEST CASE 4: Empty Tree
# =========================

root = build_tree([])

print("=== Test Case 4: Empty Tree ===")
print("Inorder        :", sol.inorder1(root))
print("Preorder       :", sol.preorder1(root))
print("Postorder      :", sol.postorder1(root))
print("Level Order    :", sol.bfs(root))
print("Height         :", sol.height1(root))
print("Size           :", sol.size1(root))
print("Reverse (iter)    :", sol.reverse_level(root))
print()
