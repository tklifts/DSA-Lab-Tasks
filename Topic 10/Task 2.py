import math
import time
import random
import matplotlib.pyplot as plt

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

# --------- Jump Search ----------
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# --------- Interpolation Search ----------
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low) //
                     (arr[high] - arr[low]))

        if pos < 0 or pos >= len(arr):
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# --------- Test Cases ----------
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print("Jump Search:", jump_search(arr, 7))              # Output: 3
print("Interpolation Search:", interpolation_search(arr, 7))  # Output: 3
print("Binary Search:", binary_search(arr, 7))          # Output: 3

# --------- Performance Comparison ----------
def measure_time(search_func, arr, target):
    start = time.time()
    search_func(arr, target)
    return time.time() - start

sizes = [1000, 5000, 10000]
jump_times = []
interpolation_times = []
binary_times = []

for size in sizes:
    data = sorted(random.sample(range(size * 10), size))
    target = data[-1]

    jump_times.append(measure_time(jump_search, data, target))
    interpolation_times.append(measure_time(interpolation_search, data, target))
    binary_times.append(measure_time(binary_search, data, target))

# --------- Plotting the Results ----------
plt.plot(sizes, jump_times, label="Jump Search", marker='o')
plt.plot(sizes, interpolation_times, label="Interpolation Search", marker='o')
plt.plot(sizes, binary_times, label="Binary Search", marker='o')
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Search Algorithm Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()
