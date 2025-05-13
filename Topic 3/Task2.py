class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return new_node  # Return node for linking if needed

    def display(self, limit=50):
        result = []
        curr = self.head
        count = 0
        while curr and count < limit:
            result.append(str(curr.data))
            curr = curr.next
            count += 1
        if curr:
            result.append("...")
        return " → ".join(result) if result else "Empty List"

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.find_loop_start(slow)
        return None

    def find_loop_start(self, meeting_point):
        start = self.head
        while start != meeting_point:
            start = start.next
            meeting_point = meeting_point.next
        return start

    def remove_loop(self):
        loop_node = self.detect_loop()
        if not loop_node:
            return False
        ptr = loop_node
        while ptr.next != loop_node:
            ptr = ptr.next
        ptr.next = None
        return True

# ---------------------------------------------
# Test Case: Create a loop and remove it
# ---------------------------------------------
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Create linked list: 1 → 2 → 3 → 4 → 5
    n1 = sll.insert_at_end(1)
    n2 = sll.insert_at_end(2)
    n3 = sll.insert_at_end(3)
    n4 = sll.insert_at_end(4)
    n5 = sll.insert_at_end(5)

    # Create a loop: 5 → 3
    n5.next = n3

    print("🔍 Checking for loop...")
    loop_start = sll.detect_loop()
    if loop_start:
        print(f"✅ Loop detected at node with value: {loop_start.data}")
    else:
        print("❌ No loop detected")

    print("\n🧹 Attempting to remove loop...")
    removed = sll.remove_loop()
    print("✅ Loop removed." if removed else "❌ No loop found.")

    print("\n📋 Linked List after loop removal:")
    print(sll.display())
