import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Sorting Algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Generate a random list of 1000 integers
data = [random.randint(1, 10000) for _ in range(1000)]

# Measure execution times
timings = {}

# Bubble Sort
bubble_data = data.copy()
start = time.time()
bubble_sort(bubble_data)
timings['Bubble Sort'] = time.time() - start

# Merge Sort
merge_data = data.copy()
start = time.time()
merge_sort(merge_data)
timings['Merge Sort'] = time.time() - start

# Quick Sort
quick_data = data.copy()
start = time.time()
sorted_quick = quick_sort(quick_data)
timings['Quick Sort'] = time.time() - start

# Display comparison table
df = pd.DataFrame(list(timings.items()), columns=['Algorithm', 'Execution Time (s)'])
print("\nExecution Time Comparison:")
print(df)

# Plot execution time graph
plt.figure(figsize=(10, 6))
plt.bar(timings.keys(), timings.values(), color=['red', 'green', 'blue'])
plt.title('Execution Time of Sorting Algorithms')
plt.ylabel('Time (seconds)')
plt.xlabel('Algorithm')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
