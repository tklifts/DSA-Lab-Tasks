import time
import random
import matplotlib.pyplot as plt

# --------- Binary Search ----------
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --------- Exponential Search ----------
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n - 1))

# --------- Fibonacci Search ----------
def fibonacci_search(arr, target):
    n = len(arr)
    fibMMm2 = 0  # (m-2)'th Fibonacci
    fibMMm1 = 1  # (m-1)'th Fibonacci
    fibM = fibMMm1 + fibMMm2  # m'th Fibonacci

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm1 + fibMMm2

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < target:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    if fibMMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    return -1

# --------- Test Cases ----------
arr = [2, 4, 8, 16, 32, 64, 128]
print("Exponential Search:", exponential_search(arr, 32))  # Output: 4
print("Fibonacci Search:", fibonacci_search(arr, 32))      # Output: 4
print("Binary Search:", binary_search(arr, 32))            # Output: 4

# --------- Performance Comparison ----------
def measure_time(search_func, arr, target):
    start = time.time()
    search_func(arr, target)
    return time.time() - start

sizes = [1000, 5000, 10000]
exp_times = []
fib_times = []
bin_times = []

for size in sizes:
    data = sorted(random.sample(range(size * 10), size))
    target = data[-1]  # Worst-case position

    exp_times.append(measure_time(exponential_search, data, target))
    fib_times.append(measure_time(fibonacci_search, data, target))
    bin_times.append(measure_time(binary_search, data, target))

# --------- Plotting the Results ----------
plt.plot(sizes, exp_times, label="Exponential Search", marker='o')
plt.plot(sizes, fib_times, label="Fibonacci Search", marker='o')
plt.plot(sizes, bin_times, label="Binary Search", marker='o')
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Search Algorithm Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()
