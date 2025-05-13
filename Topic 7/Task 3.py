import heapq

def find_k_smallest(arr, k):
    """Returns the K smallest elements using a Min-Heap."""
    if k == 0:
        return []
    
    # Build a Min-Heap and return the K smallest elements
    return heapq.nsmallest(k, arr)

def find_k_largest(arr, k):
    """Returns the K largest elements using a Max-Heap (simulated using negative values)."""
    if k == 0:
        return []
    
    # Build a Max-Heap by using negative values to simulate a Max-Heap
    return heapq.nlargest(k, arr)

# Test cases
arr = [10, 4, 3, 20, 15, 7]

# Finding the 3 smallest elements
print("K Smallest (3):", find_k_smallest(arr, 3))  # Expected Output: [3, 4, 7]

# Finding the 2 largest elements
print("K Largest (2):", find_k_largest(arr, 2))  # Expected Output: [20, 15]

# Additional test cases
arr2 = [1, 8, 2, 6, 5, 7, 9, 10]
print("K Smallest (4):", find_k_smallest(arr2, 4))  # Expected Output: [1, 2, 5, 6]
print("K Largest (3):", find_k_largest(arr2, 3))  # Expected Output: [10, 9, 8]
