class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Key to Node mapping
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    # Move the given node to the front (most recently used)
    def _move_to_front(self, node: Node):
        self._remove(node)
        self._add(node)

    # Add a node right after the head (most recently used position)
    def _add(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # Remove an existing node from the linked list
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Get the value from the cache for the given key
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1  # Key not found

    # Insert or update the key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item (tail's previous node)
                tail_node = self.tail.prev
                self._remove(tail_node)
                del self.cache[tail_node.key]
            
            # Add the new node to the front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

    # Display the current state of the cache
    def display(self):
        current = self.head.next
        cache_state = {}
        while current != self.tail:
            cache_state[current.key] = current.value
            current = current.next
        print("Cache state:", cache_state)


# Test the LRU Cache implementation
cache = LRUCache(5)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.put(4, "D")
cache.put(5, "E")
cache.display()  # Cache state: {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}

cache.get(2)  # Moves '2' to the most recently used position
cache.display()  # Cache state: {1: "A", 3: "C", 4: "D", 5: "E", 2: "B"}

cache.put(6, "F")  # Removes the least recently used key (1)
cache.display()  # Cache state: {3: "C", 4: "D", 5: "E", 2: "B", 6: "F"}

cache.put(7, "G")  # Removes the least recently used key (3)
cache.display()  # Cache state: {4: "D", 5: "E", 2: "B", 6: "F", 7: "G"}

cache.get(5)  # Moves '5' to the most recently used position
cache.display()  # Cache state: {4: "D", 2: "B", 6: "F", 7: "G", 5: "E"}
