class DynamicArray:
    def __init__(self):
        self.capacity = 1  # initial fixed capacity
        self.size = 0      # current number of elements
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if 0 < self.size <= self.capacity // 4:
            self._resize(max(1, self.capacity // 2))

    def search(self, item):
        for i in range(self.size):
            if self.array[i] == item:
                return i
        return -1

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"

# ---------------------------------------------
# Test Cases
# ---------------------------------------------

da = DynamicArray()

print("Appending elements:")
for i in range(5):
    da.append(i)
    print(da)

print("\nInserting 99 at index 2:")
da.insert(2, 99)
print(da)

print("\nDeleting element at index 3:")
da.delete(3)
print(da)

print("\nSearching for element 99:")
index = da.search(99)
print("Found at index:" if index != -1 else "Not found", index)

print("\nSearching for element 100:")
index = da.search(100)
print("Found at index:" if index != -1 else "Not found", index)
