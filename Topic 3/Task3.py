class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Delete node at specific position (1-based)
    def delete_at_position(self, position):
        if position <= 0 or not self.head:
            return False
        curr = self.head
        if position == 1:
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return True
        for _ in range(position - 1):
            if not curr:
                return False
            curr = curr.next
        if not curr:
            return False
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        return True

    # Traverse forward
    def traverse_forward(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.data))
            last = curr  # Remember the last node for reverse
            curr = curr.next
        return result, last

    # Traverse reverse from last node
    def traverse_reverse(self, tail):
        result = []
        curr = tail
        while curr:
            result.append(str(curr.data))
            curr = curr.prev
        return result

# -------------------------------------
# Test Case Demonstrating All Features
# -------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("✅ Inserting at end:")
    for val in [1, 2, 3, 4, 5]:
        dll.insert_at_end(val)

    forward, tail = dll.traverse_forward()
    print("Forward:", " → ".join(forward))

    print("✅ Reverse traversal:")
    reverse = dll.traverse_reverse(tail)
    print("Reverse:", " → ".join(reverse))

    print("\n🧹 Deleting node at position 3:")
    deleted = dll.delete_at_position(3)
    print("Deleted:", "Yes" if deleted else "No")

    forward, tail = dll.traverse_forward()
    print("Forward after deletion:", " → ".join(forward))

    print("Reverse after deletion:", " → ".join(dll.traverse_reverse(tail)))
