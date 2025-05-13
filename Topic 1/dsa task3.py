import matplotlib.pyplot as plt
import numpy as np
import math

# 1. Big-O complexity functions
def O_1(n):
    return np.ones_like(n)

def O_log_n(n):
    return np.log2(n)

def O_n(n):
    return n

def O_n_log_n(n):
    return n * np.log2(n)

def O_n_squared(n):
    return n**2

def O_2_power_n(n):
    return 2 ** n

# 2. Generate input sizes
n = np.arange(1, 1001)

# 3. Compute output values for each complexity
y1 = O_1(n)
y2 = O_log_n(n)
y3 = O_n(n)
y4 = O_n_log_n(n)
y5 = O_n_squared(n)

# For exponential, use smaller input range to avoid overflow
n_small = np.arange(1, 21)
y6 = O_2_power_n(n_small)

# 4. Plot all except exponential for clarity
plt.figure(figsize=(12, 6))
plt.plot(n, y1, label='O(1)')
plt.plot(n, y2, label='O(log n)')
plt.plot(n, y3, label='O(n)')
plt.plot(n, y4, label='O(n log n)')
plt.plot(n, y5, label='O(n²)')
plt.title('Growth of Common Time Complexities (1 ≤ n ≤ 1000)')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Separate plot for exponential
plt.figure(figsize=(8, 5))
plt.plot(n_small, y6, 'r', label='O(2ⁿ)')
plt.title('Exponential Growth: O(2ⁿ)')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
