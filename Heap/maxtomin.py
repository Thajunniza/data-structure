# ===========================================================
# Title      : Convert Max Heap to Min Heap
# Problem    : Given an array representing a Max Heap,
#              convert it in-place to a Min Heap.
# Algorithm  : Bottom-up Heapify (Heapify Down)
# ===========================================================

# Time Complexity  : O(n)   -> Heapify all non-leaf nodes
# Space Complexity : O(1)   -> In-place conversion

def convert_max(maxheap):
    """
    Convert a Max Heap to a Min Heap in-place.

    :param maxheap: List[int] representing a max heap
    :return: List[int] representing a min heap
    """
    n = len(maxheap)

    def heapify_down_small(i):
        """
        Heapify down from index i to maintain Min Heap property
        """
        while True:
            small = i
            left = 2 * i + 1
            right = 2 * i + 2

            # Compare with left child
            if left < n and maxheap[left] < maxheap[small]:
                small = left
            # Compare with right child
            if right < n and maxheap[right] < maxheap[small]:
                small = right

            # If parent is smallest, stop
            if small == i:
                break

            # Swap parent with smallest child
            maxheap[i], maxheap[small] = maxheap[small], maxheap[i]
            i = small

    # Build min heap starting from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify_down_small(i)

    return maxheap


# ===========================================================
# Test Cases
# ===========================================================
if __name__ == "__main__":
    # Test Case 1
    maxheap1 = [10, 9, 8, 7, 6, 5, 4]
    print("Original Max Heap:", maxheap1)
    print("Converted Min Heap:", convert_max(maxheap1))
    # Expected Min Heap: [4, 6, 5, 10, 7, 9, 8] (or any valid min heap)

    # Test Case 2
    maxheap2 = [20, 15, 18, 10, 12, 17, 16]
    print("\nOriginal Max Heap:", maxheap2)
    print("Converted Min Heap:", convert_max(maxheap2))
    # Expected Min Heap: [10, 12, 16, 20, 15, 17, 18] (or any valid min heap)

    # Test Case 3 - Single element
    maxheap3 = [5]
    print("\nOriginal Max Heap:", maxheap3)
    print("Converted Min Heap:", convert_max(maxheap3))
    # Expected: [5]

    # Test Case 4 - Already min heap
    maxheap4 = [1, 3, 2, 7, 6, 5, 4]
    print("\nOriginal Heap:", maxheap4)
    print("Converted Min Heap:", convert_max(maxheap4))
    # Expected: [1, 3, 2, 7, 6, 5, 4] (no change)