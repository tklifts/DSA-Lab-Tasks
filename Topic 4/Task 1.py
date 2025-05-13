# Stack using Array (Python List)
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            popped = self.head.data
            self.head = self.head.next
            self.count -= 1
            return popped
        return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.head.data
        return None

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count


# Test case function to test both stack implementations
def test_stack(stack_type):
    print(f"\nTesting {stack_type.__name__}")
    stack = stack_type()

    print("Is empty:", stack.is_empty())  # Should be True initially
    print("Pushing: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element (peek):", stack.peek())  # Should be 30
    print("Size:", stack.size())  # Should be 3
    print("Popping:", stack.pop())  # Should pop 30
    print("Top after pop:", stack.peek())  # Should be 20
    print("Is empty:", stack.is_empty())  # Should be False
    print("Final size:", stack.size())  # Should be 2

# Run tests for both stack types
if __name__ == "__main__":
    test_stack(ArrayStack)
    test_stack(LinkedListStack)
