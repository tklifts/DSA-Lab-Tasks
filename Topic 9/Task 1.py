import random
import time
import matplotlib.pyplot as plt

# ---------- Sorting Algorithms ----------

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ---------- Time Comparison Function ----------

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start

# ---------- Performance Test ----------

list_sizes = [100, 200, 300, 400, 500]
bubble_times = []
selection_times = []
insertion_times = []

for size in list_sizes:
    test_list = random.sample(range(1, size*10), size)

    bubble_times.append(measure_time(bubble_sort, test_list))
    selection_times.append(measure_time(selection_sort, test_list))
    insertion_times.append(measure_time(insertion_sort, test_list))

# ---------- Plotting the Results ----------

plt.plot(list_sizes, bubble_times, label='Bubble Sort', marker='o')
plt.plot(list_sizes, selection_times, label='Selection Sort', marker='o')
plt.plot(list_sizes, insertion_times, label='Insertion Sort', marker='o')

plt.title('Sorting Algorithm Time Comparison')
plt.xlabel('List Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()

# ---------- Test Case for Correctness ----------

arr = [64, 25, 12, 22, 11]
print("Original:", arr)
print("Bubble Sort:", bubble_sort(arr))
print("Selection Sort:", selection_sort(arr))
print("Insertion Sort:", insertion_sort(arr))
