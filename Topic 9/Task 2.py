import random
import time
import matplotlib.pyplot as plt

# ---------- Merge Sort ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# ---------- Quick Sort ----------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ---------- Timing Function ----------
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start

# ---------- Test Case for Correctness ----------
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original:", arr)
print("Quick Sort:", quick_sort(arr))
print("Merge Sort:", merge_sort(arr))

# ---------- Performance Comparison ----------
sizes = [1000, 5000, 10000]
quick_times = []
merge_times = []

for size in sizes:
    test_data = random.sample(range(size * 10), size)
    quick_times.append(measure_time(quick_sort, test_data))
    merge_times.append(measure_time(merge_sort, test_data))

# ---------- Plot Results ----------
plt.plot(sizes, quick_times, label="Quick Sort", marker='o')
plt.plot(sizes, merge_times, label="Merge Sort", marker='o')
plt.title("Quick Sort vs Merge Sort Performance")
plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
