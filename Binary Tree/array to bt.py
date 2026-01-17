from collections import deque
class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def arrtobt(self,arr):
        n = len(arr)
        if n == 0 or arr[0] == None:
            return None
        root = Node(arr[0])
        q = deque([root])
        i = 1
        while i < n and q:
            node = q.popleft()

            if i < n and arr[i] is not None:
                leftNode = Node(arr[i])
                node.left = leftNode
                q.append(leftNode)
            
            i += 1

            if i < n and arr[i] is not None:
                rightNode = Node(arr[i])
                node.right = rightNode
                q.append(rightNode)
            
            i += 1
        return root

def level_order(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)

    # Trim trailing None values for readability
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Normal binary tree
    arr1 = [3, 9, 20, None, None, 15, 7]
    root1 = sol.arrtobt(arr1)
    print("Test 1:", level_order(root1))
    # Expected: [3, 9, 20, None, None, 15, 7]

    # Test Case 2: Single node
    arr2 = [1]
    root2 = sol.arrtobt(arr2)
    print("Test 2:", level_order(root2))
    # Expected: [1]

    # Test Case 3: Empty array
    arr3 = []
    root3 = sol.arrtobt(arr3)
    print("Test 3:", level_order(root3))
    # Expected: []

    # Test Case 4: Left-skewed tree
    arr4 = [1, 2, None, 3, None, 4]
    root4 = sol.arrtobt(arr4)
    print("Test 4:", level_order(root4))
    # Expected: [1, 2, None, 3, None, 4]

    # Test Case 5: Complete binary tree
    arr5 = [1, 2, 3, 4, 5, 6, 7]
    root5 = sol.arrtobt(arr5)
    print("Test 5:", level_order(root5))
    # Expected: [1, 2, 3, 4, 5, 6, 7]

