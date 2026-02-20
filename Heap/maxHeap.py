"""
Max Heap (Binary Heap, Array-Based, 0-Indexed)

This module implements a Max Heap using a dynamic array (Python list).
The heap maintains the invariant: for every node i (except the root),
heap[i] >= heap[left(i)] and heap[i] >= heap[right(i)] when children exist.

Index formulas (0-based):
    parent(i) = (i - 1) // 2
    left(i)   = 2*i + 1
    right(i)  = 2*i + 2

Core operations:
    - insert(val): O(log n)     -> push value and sift up until heap property holds.
    - delete(): O(log n)        -> remove and return current max; sift down root.
    - getMax(): O(1)            -> peek max element or None if empty.
"""

class MaxHeap:
    """Array-backed binary max-heap (0-indexed)."""

    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []

    def insert(self, val):
        """
        Insert a value into the heap and restore the heap invariant.

        Algorithm:
            1) Append val at the end.
            2) Sift up: while val > parent, swap with parent.

        Time: O(log n)
        Space: O(1) auxiliary (in-place)
        """
        self.heap.append(val)
        self.__heapifyUp(len(self.heap) - 1)

    def delete(self):
        """
        Remove and return the maximum element from the heap.

        Algorithm:
            1) If empty -> return None.
            2) If size == 1 -> pop and return the only element.
            3) Swap root with last element.
            4) Pop the last (former root) -> this is the max to return.
            5) Sift down the new root to restore the heap property.

        Time: O(log n)
        Space: O(1) auxiliary (in-place)
        """
        n = len(self.heap)
        if n == 0:
            return None
        if n == 1:
            return self.heap.pop()

        # Move current max (root) to the end, pop it, then repair from root
        self.heap[0], self.heap[n - 1] = self.heap[n - 1], self.heap[0]
        top = self.heap.pop()
        self.__heapifyDown(0)
        return top

    def getMax(self):
        """
        Return the maximum element without removing it.

        Returns:
            The root element (max) or None if the heap is empty.

        Time: O(1)
        """
        if self.heap:
            return self.heap[0]
        return None

    # ---------- index helpers (0-based) ----------
    def _parent(self, i):
        """Return the parent index of i (0-based)."""
        return (i - 1) // 2

    def _left(self, i):
        """Return the left child index of i (0-based)."""
        return 2 * i + 1

    def _right(self, i):
        """Return the right child index of i (0-based)."""
        return 2 * i + 2

    # ---------- heap maintenance ----------
    def __heapifyUp(self, i):
        """
        Sift-up from index i until the heap property holds.

        Invariant:
            While the current node is larger than its parent,
            swap them and continue from the parent position.

        Time: O(log n) in the worst case (height of the heap).
        """
        if i <= 0:
            return
        p = self._parent(i)
        if self.heap[p] < self.heap[i]:
            # Swap with parent and continue sifting up
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            self.__heapifyUp(p)
        else:
            return

    def __heapifyDown(self, i):
        """
        Sift-down from index i until the heap property holds.

        Algorithm:
            Choose the largest among (i, left(i), right(i)), swap with that child,
            and continue from the child until no violation remains.

        Time: O(log n) in the worst case.
        """
        n = len(self.heap)
        while True:
            l, r = self._left(i), self._right(i)
            largest = i

            if l < n and self.heap[l] > self.heap[largest]:
                largest = l
            if r < n and self.heap[r] > self.heap[largest]:
                largest = r

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    # ---------- debug helper ----------
    def printHeap(self):
        """Print the underlying array representation of the heap."""
        for val in self.heap:
            print(val, end=" -> ")
        print("")
        

# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(10)
    heap.printHeap()
    heap.insert(20)
    heap.printHeap()
    heap.insert(12)
    heap.insert(22)
    heap.insert(50)
    heap.printHeap()

    print(f"Get the Max Value: {heap.getMax()}")
    print(f"Deleted: {heap.delete()}")
    heap.printHeap()

    print(f"Get the Max Value: {heap.getMax()}")
    print(f"Deleted: {heap.delete()}")
    heap.printHeap()

    print(f"Get the Max Value: {heap.getMax()}")
    print(f"Deleted: {heap.delete()}")
    heap.printHeap()

    print(f"Get the Max Value: {heap.getMax()}")
    print(f"Deleted: {heap.delete()}")
    heap.printHeap()

    print(f"Get the Max Value: {heap.getMax()}")