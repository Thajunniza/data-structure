"""
===========================================================
DOUBLY LINKED LIST IMPLEMENTATION
===========================================================
A Doubly Linked List is a linear data structure where each
node contains:
    1. Value
    2. Pointer to the previous node
    3. Pointer to the next node

This allows traversal in both forward and backward directions.

-----------------------------------------------------------
Time & Space Complexity
-----------------------------------------------------------
Insertion / Deletion at head or tail : O(1)
Insertion / Deletion at index        : O(n)
Traversal                            : O(n)
Space                                : O(n)
===========================================================
"""


class Node:
    """
    Represents a single node in a Doubly Linked List
    """

    def __init__(self, val):
        self.val = val        # Data stored in the node
        self.prev = None     # Pointer to previous node
        self.next = None     # Pointer to next node


class DoublyLinkedList:
    """
    Doubly Linked List class supporting common operations
    """

    def __init__(self):
        self.head = None     # First node of the list
        self.tail = None     # Last node of the list
        self.size = 0        # Total number of nodes

    # ---------------------------------------------------
    # Utility Operations
    # ---------------------------------------------------
    def is_empty(self):
        """Check if the list is empty"""
        return self.size == 0

    def get_length(self):
        """Return total number of nodes"""
        return self.size

    def print_list(self):
        """Traverse and print the list"""
        curr = self.head
        while curr:
            print(curr.val, end=" <-> " if curr.next else "\n")
            curr = curr.next

    # ---------------------------------------------------
    # Insertion Operations
    # ---------------------------------------------------
    def append(self, val):
        """
        Insert a node at the end of the list
        Time Complexity: O(1)
        """
        new_node = Node(val)

        if self.is_empty():
            # First node in the list
            self.head = self.tail = new_node
        else:
            # Attach at the tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def prepend(self, val):
        """
        Insert a node at the beginning of the list
        Time Complexity: O(1)
        """
        new_node = Node(val)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert(self, val, index):
        """
        Insert a node at a specific index
        Time Complexity: O(n)
        """
        if index < 0 or index > self.size:
            raise IndexError("Invalid Index")

        if index == 0:
            self.prepend(val)
            return
        if index == self.size:
            self.append(val)
            return

        curr = self._get_node_at_index(index)
        new_node = Node(val)

        # Re-wire pointers
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = curr
        curr.prev = new_node

        self.size += 1

    # ---------------------------------------------------
    # Deletion Operations
    # ---------------------------------------------------
    def pop(self):
        """
        Delete and return the first node's value
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from empty list")

        val = self.head.val
        self.delete_first()
        return val

    def delete_first(self):
        """
        Delete the first node
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Delete from empty list")

        if self.size == 1:
            # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def delete_last(self):
        """
        Delete the last node
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Delete from empty list")

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

    def delete_at_index(self, index):
        """
        Delete node at a specific index
        Time Complexity: O(n)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Invalid Index")

        if index == 0:
            self.delete_first()
            return
        if index == self.size - 1:
            self.delete_last()
            return

        curr = self._get_node_at_index(index)

        # Re-wire pointers
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1

    def delete(self, val):
        """
        Delete the first occurrence of a value
        Time Complexity: O(n)
        """
        curr = self.head

        while curr:
            if curr.val == val:
                if curr == self.head:
                    self.delete_first()
                elif curr == self.tail:
                    self.delete_last()
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self.size -= 1
                return
            curr = curr.next

        raise ValueError("Value not found")

    # ---------------------------------------------------
    # Internal Helper Method
    # ---------------------------------------------------
    def _get_node_at_index(self, index):
        """
        Optimized traversal:
        - Start from head if index is in first half
        - Start from tail if index is in second half
        """
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr

    def clear(self):
        """
        Delete all nodes from the list
        """
        self.head = self.tail = None
        self.size = 0


# ===========================================================
# Test Results
# ===========================================================
# Example run
if __name__ == "__main__":
    d1 = DoublyLinkedList()       
    d1.print_list()
    d1.append(1)
    d1.append(2)
    d1.print_list()
    d1.prepend(3)
    d1.prepend(4)
    d1.print_list()
    d1.insert(5,1)
    print(d1.get_length())
    d1.print_list()
    d1.delete_first()
    d1.print_list()
    d1.delete_last()
    d1.print_list()
    d1.delete_at_index(1)
    d1.print_list()
    d1.clear()
    print(d1.get_length())
            
