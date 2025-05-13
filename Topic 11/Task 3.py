class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # This will map key to node in the doubly linked list
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail  # Initially head's next is tail
        self.tail.prev = self.head  # Initially tail's prev is head
        
    # Remove node from the linked list
    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    # Add node to the front (right after head)
    def add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    # Get the value of the key if present in the cache
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Remove it from its current position
            self.add_to_front(node)  # Add it to the front (most recent)
            return node.value
        return -1
    
    # Insert key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Remove it from its current position
        else:
            node = Node(key, value)
            self.cache[key] = node
        
        # Add the new/updated node to the front (most recent)
        self.add_to_front(node)
        
        # If the cache exceeds the capacity, remove the LRU item
        if len(self.cache) > self.capacity:
            lru = self.tail.prev  # LRU item is right before the tail
            self.remove(lru)  # Remove the LRU item from the linked list
            del self.cache[lru.key]  # Delete the LRU item from the cache

# Test the LRU Cache
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))  # Output: "A"
cache.put(3, "C")  # Removes least recently used key (2)
print(cache.get(2))  # Output: -1 (not found)
cache.put(4, "D")  # Removes least recently used key (1)
print(cache.get(1))  # Output: -1 (not found)
print(cache.get(3))  # Output: "C"
print(cache.get(4))  # Output: "D"
