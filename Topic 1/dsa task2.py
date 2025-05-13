import time
import matplotlib.pyplot as plt
import pandas as pd
from functools import lru_cache

# 1. Recursive Fibonacci (naive)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# 2. Iterative Fibonacci
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 3. Recursive Fibonacci with memoization
@lru_cache(maxsize=None)
def fib_memoized(n):
    if n <= 1:
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)

# Values of n to test
test_values = [10, 20, 30, 40]
timings = {'n': [], 'Recursive': [], 'Iterative': [], 'Memoized': []}

# Measure execution times
for n in test_values:
    timings['n'].append(n)
    
    # Recursive
    start = time.time()
    fib_recursive(n)
    timings['Recursive'].append(time.time() - start)

    # Iterative
    start = time.time()
    fib_iterative(n)
    timings['Iterative'].append(time.time() - start)

    # Memoized
    start = time.time()
    fib_memoized(n)
    timings['Memoized'].append(time.time() - start)

# Create DataFrame
df = pd.DataFrame(timings)
print("\nExecution Time Comparison (in seconds):")
print(df)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['n'], df['Recursive'], 'r-o', label='Recursive')
plt.plot(df['n'], df['Iterative'], 'g-o', label='Iterative')
plt.plot(df['n'], df['Memoized'], 'b-o', label='Memoized Recursive')
plt.xlabel('n (Fibonacci number)')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci: Recursive vs Iterative vs Memoized')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
