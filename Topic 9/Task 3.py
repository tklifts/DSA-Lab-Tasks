import random
import time
import matplotlib.pyplot as plt

# ---------- Heap Sort ----------
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

# ---------- Counting Sort ----------
def counting_sort(arr):
    arr = arr.copy()
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])
    return output

# ---------- Time Measurement ----------
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    return time.time() - start

# ---------- Correctness Test ----------
arr1 = [4, 10, 3, 5, 1]
arr2 = [1, 4, 1, 2, 7, 5, 2]

print("Heap Sort:", heap_sort(arr1))         # Output: [1, 3, 4, 5, 10]
print("Counting Sort:", counting_sort(arr2)) # Output: [1, 1, 2, 2, 4, 5, 7]

# ---------- Performance Comparison ----------
sizes = [1000, 5000, 10000, 20000]
heap_times = []
count_times = []

for size in sizes:
    heap_data = random.sample(range(1, size * 10), size)
    count_data = random.choices(range(1000), k=size)  # Limited range for counting sort

    heap_times.append(measure_time(heap_sort, heap_data))
    count_times.append(measure_time(counting_sort, count_data))

# ---------- Plot Results ----------
plt.plot(sizes, heap_times, label='Heap Sort', marker='o')
plt.plot(sizes, count_times, label='Counting Sort', marker='o')
plt.title("Heap Sort vs Counting Sort Performance")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
