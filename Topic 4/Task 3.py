# Circular Queue Implementation
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, element):
        if self.is_full():
            print("Queue is Full!")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        dequeued_element = self.queue[self.front]
        if self.front == self.rear:  # Queue has only one element left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return dequeued_element

    def front_element(self):
        if not self.is_empty():
            return self.queue[self.front]
        return None

    def rear_element(self):
        if not self.is_empty():
            return self.queue[self.rear]
        return None

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            idx = self.front
            while idx != self.rear:
                print(self.queue[idx], end=" ")
                idx = (idx + 1) % self.size
            print(self.queue[self.rear])


# Linear Queue Implementation (using a Python list)
class LinearQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def enqueue(self, element):
        if len(self.queue) == self.size:
            print("Queue is Full!")
            return
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        return self.queue.pop(0)

    def front_element(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def rear_element(self):
        if not self.is_empty():
            return self.queue[-1]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            print("Queue:", *self.queue)


# Test cases to demonstrate Circular Queue and Linear Queue operations
def test_queues():
    # Test Circular Queue
    print("Testing Circular Queue (Size 5):")
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)
    cq.display()  # Expected output: 10 20 30 40 50
    print("Front element:", cq.front_element())  # Expected output: 10
    print("Rear element:", cq.rear_element())  # Expected output: 50
    cq.dequeue()
    cq.enqueue(60)
    cq.display()  # Expected output: 20 30 40 50 60
    print("Front element:", cq.front_element())  # Expected output: 20
    print("Rear element:", cq.rear_element())  # Expected output: 60

    # Test Linear Queue
    print("\nTesting Linear Queue (Size 5):")
    lq = LinearQueue(5)
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    lq.enqueue(40)
    lq.enqueue(50)
    lq.display()  # Expected output: Queue: 10 20 30 40 50
    print("Front element:", lq.front_element())  # Expected output: 10
    print("Rear element:", lq.rear_element())  # Expected output: 50
    lq.dequeue()
    lq.enqueue(60)
    lq.display()  # Expected output: Queue: 20 30 40 50 60
    print("Front element:", lq.front_element())  # Expected output: 20
    print("Rear element:", lq.rear_element())  # Expected output: 60

# Run the test cases
if __name__ == "__main__":
    test_queues()
