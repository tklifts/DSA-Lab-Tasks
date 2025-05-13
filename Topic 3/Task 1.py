class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Insert at specific position (1-based)
    def insert_at_position(self, data, position):
        if position <= 0:
            raise IndexError("Position must be 1 or greater")
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        for _ in range(position - 2):
            if not curr:
                raise IndexError("Position out of bounds")
            curr = curr.next
        if not curr:
            raise IndexError("Position out of bounds")
        new_node.next = curr.next
        curr.next = new_node

    # Delete by value
    def delete_by_value(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    # Search for value
    def search(self, value):
        curr = self.head
        pos = 1
        while curr:
            if curr.data == value:
                return pos
            curr = curr.next
            pos += 1
        return -1

    # Display linked list
    def display(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return " → ".join(result) if result else "Empty List"

# ---------------------------------------------------
# Test Cases
# ---------------------------------------------------

if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("✅ Initial list:")
    print(sll.display())

    print("\n✅ Insert at end:")
    for val in [1, 2, 3, 4]:
        sll.insert_at_end(val)
        print("After inserting", val, "→", sll.display())

    print("\n✅ Insert 5 at end:")
    sll.insert_at_end(5)
    print("List:", sll.display())

    print("\n✅ Insert 0 at beginning:")
    sll.insert_at_beginning(0)
    print("List:", sll.display())

    print("\n✅ Insert 9 at position 4:")
    sll.insert_at_position(9, 4)
    print("List:", sll.display())

    print("\n✅ Delete node with value 3:")
    deleted = sll.delete_by_value(3)
    print("Deleted:", deleted)
    print("List:", sll.display())

    print("\n✅ Search for value 4:")
    pos = sll.search(4)
    print("Found at position:" if pos != -1 else "Not found", pos)

    print("\n✅ Search for value 10:")
    pos = sll.search(10)
    print("Found at position:" if pos != -1 else "Not found", pos)

    print("\n✅ Final linked list:")
    print(sll.display())
