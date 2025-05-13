# Node class for Chaining (Linked List)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash Table Class
class HashTable:
    def __init__(self, size, method='chaining'):
        self.size = size
        self.method = method
        self.table = [None] * size
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    # Chaining (Linked List) Insertion
    def insert_chaining(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node
    
    # Chaining (Linked List) Search
    def get_chaining(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    # Chaining (Linked List) Deletion
    def delete_chaining(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next
        return
    
    # Linear Probing (Open Addressing) Insertion
    def insert_linear_probing(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update value if key exists
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash Table is full!")
        self.table[index] = (key, value)
    
    # Linear Probing (Open Addressing) Search
    def get_linear_probing(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None
    
    # Linear Probing (Open Addressing) Deletion
    def delete_linear_probing(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        return

    # Public insert, get, and delete methods based on collision resolution method
    def insert(self, key, value):
        if self.method == 'chaining':
            self.insert_chaining(key, value)
        elif self.method == 'linear_probing':
            self.insert_linear_probing(key, value)
    
    def get(self, key):
        if self.method == 'chaining':
            return self.get_chaining(key)
        elif self.method == 'linear_probing':
            return self.get_linear_probing(key)
    
    def delete(self, key):
        if self.method == 'chaining':
            self.delete_chaining(key)
        elif self.method == 'linear_probing':
            self.delete_linear_probing(key)

    def display(self):
        if self.method == 'chaining':
            for i in range(self.size):
                current = self.table[i]
                if current:
                    chain = []
                    while current:
                        chain.append((current.key, current.value))
                        current = current.next
                    print(f"Index {i}: {chain}")
                else:
                    print(f"Index {i}: None")
        elif self.method == 'linear_probing':
            for i in range(self.size):
                print(f"Index {i}: {self.table[i]}")

# ---- Test Cases ----

# Using Chaining (Linked List) collision resolution
print("Using Chaining:")
ht = HashTable(10, 'chaining')
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("address", "123 Street")
print(ht.get("name"))  # Output: Alice
ht.delete("age")
print(ht.get("age"))   # Output: None
ht.display()

print("\n")

# Using Linear Probing (Open Addressing) collision resolution
print("Using Linear Probing:")
ht2 = HashTable(10, 'linear_probing')
ht2.insert("name", "Alice")
ht2.insert("age", 25)
ht2.insert("address", "123 Street")
print(ht2.get("name"))  # Output: Alice
ht2.delete("age")
print(ht2.get("age"))   # Output: None
ht2.display()
