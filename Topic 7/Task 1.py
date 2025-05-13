class Heap:
    def __init__(self, heap_type="min"):
        """Initialize the heap. Choose 'min' for Min-Heap or 'max' for Max-Heap."""
        self.heap = []
        self.heap_type = heap_type  # Either 'min' or 'max'

    def _parent(self, index):
        return (index - 1) // 2
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2

    def _compare(self, index1, index2):
        """Helper function to compare values based on heap type."""
        if self.heap_type == "min":
            return self.heap[index1] < self.heap[index2]
        else:
            return self.heap[index1] > self.heap[index2]

    def _heapify_up(self, index):
        """Ensure the heap property is maintained while inserting."""
        while index > 0 and self._compare(index, self._parent(index)):
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index):
        """Ensure the heap property is maintained after extracting the root."""
        size = len(self.heap)
        while self._left_child(index) < size:
            smaller_or_larger = self._left_child(index)
            right = self._right_child(index)
            if right < size and self._compare(right, smaller_or_larger):
                smaller_or_larger = right
            
            if self._compare(smaller_or_larger, index):
                break

            self.heap[index], self.heap[smaller_or_larger] = self.heap[smaller_or_larger], self.heap[index]
            index = smaller_or_larger

    def insert(self, value):
        """Insert a value into the heap while maintaining the heap property."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_root(self):
        """Remove and return the root of the heap."""
        if len(self.heap) == 0:
            raise IndexError("extract_root from empty heap")
        root = self.heap[0]
        # Replace the root with the last element and reheapify
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self._heapify_down(0)
        return root

    def peek(self):
        """Return the root element without removing it."""
        if len(self.heap) == 0:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def heapify(self, array):
        """Build the heap from an unsorted array."""
        self.heap = array
        start = len(self.heap) // 2 - 1
        for i in range(start, -1, -1):
            self._heapify_down(i)

# Test cases to demonstrate Min-Heap and Max-Heap functionality

# Min-Heap Test
min_heap = Heap("min")
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
print("Min-Heap Root (Extracted):", min_heap.extract_root())  # Expected Output: 2
print("Min-Heap Root (Peek):", min_heap.peek())  # Expected Output: 5

# Max-Heap Test
max_heap = Heap("max")
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
print("Max-Heap Root (Extracted):", max_heap.extract_root())  # Expected Output: 20
print("Max-Heap Root (Peek):", max_heap.peek())  # Expected Output: 10

# Heapify an unsorted array into a Min-Heap
unsorted_array = [10, 5, 20, 2]
min_heap2 = Heap("min")
min_heap2.heapify(unsorted_array)
print("Min-Heap after Heapify:", min_heap2.heap)  # Expected Output: [2, 5, 20, 10]
