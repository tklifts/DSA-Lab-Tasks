import time
import random
import matplotlib.pyplot as plt

# --------- Linear Search ----------
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# --------- Binary Search ----------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --------- Correctness Test ----------
arr = [10, 23, 45, 70, 11, 15]
sorted_arr = sorted(arr)

print("Linear Search Result:", linear_search(arr, 45))       # Output: 2
print("Binary Search Result:", binary_search(sorted_arr, 45))  # Output: 3

# --------- Performance Comparison ----------
def measure_search_time(search_func, arr, target):
    start = time.time()
    search_func(arr, target)
    return time.time() - start

sizes = [1000, 5000, 10000]
linear_times = []
binary_times = []

for size in sizes:
    data = random.sample(range(size * 2), size)
    sorted_data = sorted(data)
    target = data[-1]  # Worst case (last element)

    linear_times.append(measure_search_time(linear_search, data, target))
    binary_times.append(measure_search_time(binary_search, sorted_data, target))

# --------- Plotting the Performance ----------
plt.plot(sizes, linear_times, label="Linear Search", marker='o')
plt.plot(sizes, binary_times, label="Binary Search", marker='o')
plt.title("Linear Search vs Binary Search Performance")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
