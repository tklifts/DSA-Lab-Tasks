import random
import string
import time

# Linked List Node for Chaining
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash Table with Chaining (Separate Chaining)
class HashTableChaining:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        new_node = Node(key, value)

        # If no node at index, place new node there
        if not self.table[idx]:
            self.table[idx] = new_node
        else:
            # Collision occurred, add node to the linked list
            current = self.table[idx]
            while current:
                if current.key == key:  # If key already exists, update value
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = new_node

    def get(self, key):
        idx = self._hash(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        idx = self._hash(key)
        current = self.table[idx]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[idx] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            if current:
                print(f"Index {i}: ", end="")
                while current:
                    print(f"({current.key}, {current.value})", end=" -> ")
                    current = current.next
                print()

# Hash Table with Open Addressing (Linear Probing)
class HashTableOpenAddressing:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, idx):
        return (idx + 1) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        if self.table[idx] is None:
            self.table[idx] = (key, value)
        else:
            # Collision occurred, apply linear probing
            while self.table[idx] is not None:
                if self.table[idx][0] == key:  # If key already exists, update value
                    self.table[idx] = (key, value)
                    return
                idx = self._probe(idx)
            self.table[idx] = (key, value)

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx]:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = self._probe(idx)
            if idx == start_idx:  # All slots have been checked
                break
        return None

    def delete(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx]:
            if self.table[idx][0] == key:
                self.table[idx] = None
                return True
            idx = self._probe(idx)
            if idx == start_idx:
                break
        return False

    def display(self):
        for i in range(self.size):
            if self.table[i]:
                print(f"Index {i}: {self.table[i]}")

# Test functions for comparing Chaining vs Open Addressing
def random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def test_hash_table_collisions():
    # Create hash tables
    size = 50
    chaining_table = HashTableChaining(size)
    open_addressing_table = HashTableOpenAddressing(size)

    # Generate random key-value pairs
    data = [(random_string(), random.randint(1, 1000)) for _ in range(1000)]

    # Time Chaining Insertions
    start_time = time.time()
    for key, value in data:
        chaining_table.insert(key, value)
    chaining_insert_time = time.time() - start_time

    # Time Open Addressing Insertions
    start_time = time.time()
    for key, value in data:
        open_addressing_table.insert(key, value)
    open_addressing_insert_time = time.time() - start_time

    # Time Chaining Lookups
    start_time = time.time()
    for key, _ in data:
        chaining_table.get(key)
    chaining_lookup_time = time.time() - start_time

    # Time Open Addressing Lookups
    start_time = time.time()
    for key, _ in data:
        open_addressing_table.get(key)
    open_addressing_lookup_time = time.time() - start_time

    # Results
    print(f"Chaining Insert Time: {chaining_insert_time:.5f} seconds")
    print(f"Open Addressing Insert Time: {open_addressing_insert_time:.5f} seconds")
    print(f"Chaining Lookup Time: {chaining_lookup_time:.5f} seconds")
    print(f"Open Addressing Lookup Time: {open_addressing_lookup_time:.5f} seconds")

    # Compare performance
    print("\n--- Performance Summary ---")
    if chaining_insert_time < open_addressing_insert_time:
        print("Chaining performs better for insertions.")
    else:
        print("Open Addressing performs better for insertions.")

    if chaining_lookup_time < open_addressing_lookup_time:
        print("Chaining performs better for lookups.")
    else:
        print("Open Addressing performs better for lookups.")

# Run the test
if __name__ == "__main__":
    test_hash_table_collisions()
