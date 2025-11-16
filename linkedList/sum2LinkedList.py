"""
Sum Two Linked Lists

We need to sum two linked lists and return the sum embedded in another linked list.

Example:
llist1: 5 -> 6 -> 3   (represents 365)
llist2: 8 -> 4 -> 2   (represents 248)

365 + 248 = 613

Result list should be:
3 -> 1 -> 6   (represents 613, stored in reverse order)
"""


class Node:
    def __init__(self, data):
        # Each node stores a single digit and a pointer to the next node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Head points to the first node of the linked list
        self.head = None

    def append(self, data):
        """
        Append the data at the end of the list.

        Steps:
        1. Create a new node for the data.
        2. If the linked list is empty, mark the head as the new node.
        3. Else, traverse from head to the last node and link new node at the end.
        """
        new_node = Node(data)

        # If the list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, find the last node and append
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """
        Print out the entries of a linked list.

        Start from head and keep moving to `next` until None.
        """
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    # ─────────────────────────────────────────────
    # Approach 1: Convert to Integer, Add, Convert Back
    # ─────────────────────────────────────────────
    def sum_two_lists1(self, llist):
        """
        Sum two linked lists by:
        1. Converting each linked list into a full integer.
        2. Adding the two integers.
        3. Converting the sum back into a new linked list.

        Time Complexity:
            - O(n + m) to traverse both lists and build strings.
            - Integer conversion & string reversal are also O(n + m).
            => Overall: O(n + m)

        Space Complexity:
            - Extra strings to store digits: O(n + m)
            - Result linked list: O(k), where k is number of digits in sum.
        """
        result = LinkedList()
        a = 0
        b = 0

        # If both lists are empty, return empty result
        if not self.head and not llist.head:
            return result

        def reversell(ll):
            """
            Build a string from the linked list digits,
            then reverse the string to get the correct integer order.

            Example:
                list: 5 -> 6 -> 3 (stored as 5,6,3)
                data = "563"
                reversed = "365"  (actual number)
            """
            curr = ll.head
            data = ""
            while curr:
                data += str(curr.data)
                curr = curr.next
            # Reverse the string so that least significant digit is at the end
            return data[::-1]

        # Convert self list to integer if not empty
        if self.head:
            a = int(reversell(self))

        # Convert other list to integer if not empty
        if llist.head:
            b = int(reversell(llist))

        total = a + b  # sum of two integers

        # Reverse again to store result back in "reverse-order" linked list
        revsum = str(total)[::-1]
        for ch in revsum:
            result.append(int(ch))

        return result

    # ─────────────────────────────────────────────
    # Approach 2: Digit-by-Digit Addition with Carry
    # ─────────────────────────────────────────────
    def sum_two_lists2(self, llist):
        """
        Proper DSA approach:
        - Add digits node-by-node like we do column-wise addition on paper.
        - Carry is propagated as we go.

        We assume:
        - Each node stores a single digit.
        - Digits are stored in reverse order (1's place at head).

        Example:
            5 -> 6 -> 3   (365)
            8 -> 4 -> 2   (248)

            Addition steps (by position):
            5 + 8 = 13  -> write 3, carry 1
            6 + 4 + 1 = 11 -> write 1, carry 1
            3 + 2 + 1 = 6  -> write 6, carry 0

            Result: 3 -> 1 -> 6  (which is 613)

        Time Complexity:
            - We traverse both lists once: O(n + m)

        Space Complexity:
            - Only extra variables (carry, a, b): O(1) extra space
            - Result list: O(k) digits in sum (this is required output space)
        """
        result = LinkedList()

        p = self.head      # pointer for first list
        q = llist.head     # pointer for second list
        carry = 0          # carry from previous digit addition

        # Loop runs while there is at least one node left in either list
        while p or q:
            # If p is exhausted, use 0 as digit
            if not p:
                a = 0
            else:
                a = p.data

            # If q is exhausted, use 0 as digit
            if not q:
                b = 0
            else:
                b = q.data

            # Sum of both digits + carry from previous step
            s = a + b + carry

            if s >= 10:
                # If sum >= 10, we have a carry
                remainder = s % 10   # last digit (ones place)
                result.append(remainder)
                carry = 1            # carry over to next position
            else:
                # No carry, directly store the sum as digit
                carry = 0
                result.append(s)

            # Move pointers forward if possible
            if p:
                p = p.next
            if q:
                q = q.next

        # After processing all nodes, if there is a leftover carry (e.g. 9+1=10)
        if carry:
            result.append(carry)

        return result


# ─────────────────────────────────────────────
# Execution / Test
# ─────────────────────────────────────────────

llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(3)

llist1 = LinkedList()
llist1.append(8)
llist1.append(4)
llist1.append(2)

print("Approach 1 (int conversion):")
sum1 = llist.sum_two_lists1(llist1)
sum1.print_list()

print("Approach 2 (digit-by-digit with carry):")
sum2 = llist.sum_two_lists2(llist1)
sum2.print_list()
