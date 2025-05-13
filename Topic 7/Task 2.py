import heapq

class PriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue using a Min-Heap."""
        self.heap = []

    def enqueue(self, value, priority):
        """Insert an element based on its priority."""
        # heapq is a Min-Heap, so we store the tuple (priority, value).
        # Lower priority number means higher priority.
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        """Remove and return the element with the highest priority."""
        if len(self.heap) == 0:
            raise IndexError("dequeue from empty priority queue")
        # Pop the smallest element, which is the one with the highest priority
        return heapq.heappop(self.heap)[1]

    def peek(self):
        """Return the highest priority element without removing it."""
        if len(self.heap) == 0:
            raise IndexError("peek from empty priority queue")
        return self.heap[0][1]

# Test cases demonstrating the Priority Queue operations

# Create a PriorityQueue instance
pq = PriorityQueue()

# Enqueue tasks with different priorities
pq.enqueue("Task A", 3)  # Priority 3
pq.enqueue("Task B", 1)  # Priority 1 (highest priority)
pq.enqueue("Task C", 2)  # Priority 2

# Test: Dequeue highest priority task (Task B)
print("Dequeued:", pq.dequeue())  # Expected Output: Task B

# Test: Peek the highest priority task (now Task C with priority 2)
print("Peek:", pq.peek())  # Expected Output: Task C

# Test: Dequeue remaining tasks
print("Dequeued:", pq.dequeue())  # Expected Output: Task C
print("Dequeued:", pq.dequeue())  # Expected Output: Task A

# Test empty priority queue
try:
    pq.dequeue()
except IndexError as e:
    print("Error:", e)  # Expected Output: Error: dequeue from empty priority queue
