# factorial.py - Gower Campbell  
# Comparing recursion vs iteration for factorial calculation, with performance analysis and stack safety.

import time
import sys

# Increase recursion limit for large inputs (use with caution)
sys.setrecursionlimit(2000)

def factorial_recursive(n, memo={}):
    """The function calculates factorials by calling itself (recursion) and remembers past results (memoization) to speed up repeated calculations."""
    if n in memo:
        return memo[n]
    if n == 0:  # Base case
        return 1
    memo[n] = n * factorial_recursive(n - 1, memo)  # Recursive case with memoization
    return memo[n]

def factorial_iterative(n):
    """The function uses a loop instead of recursion to calculate factorials, making it faster, more memory-efficient, and safer for large inputs."""
    result = 1
    for i in range(2, n + 1):  # Start from 2, as multiplying by 1 is redundant
        result *= i
    return result

def measure_time(func, n):
    """A helper function that tracks how long a factorial function takes to execute, helping compare performance""
    start_time = time.time()
    result = func(n)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

if __name__ == "__main__":
    n = 500  # Larger number to show performance differences

    # Measure recursive execution time
    recursive_result, recursive_time = measure_time(factorial_recursive, n)

    # Measure iterative execution time
    iterative_result, iterative_time = measure_time(factorial_iterative, n)

    # Print results
    print(f"Recursive {n}! computed (Time: {recursive_time:.8f} sec)")
    print(f"Iterative {n}! computed (Time: {iterative_time:.8f} sec)")

    # Observations
    print("\n🔍 Observations:")
    print("- Recursion with memoization helps, but iteration is still faster for large inputs.")
    print("- Iteration avoids stack overflow and is generally the preferred approach.")
    print("- Recursion shines for problems with inherent recursive structure (e.g., trees, divide & conquer).")
