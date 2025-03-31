# fibonacci.py - Gower Campbell  
# Comparing recursive, memoized, and iterative Fibonacci implementations.  
# Explanation of Fibonacci sequence and its applications.

# Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# The sequence starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Mathematical definition:
# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2) for n > 1

# Fibonacci numbers show up naturally in:
# - Nature (like the pattern of petals in flowers and the spiral arrangement of leaves)
# - Algorithms (for searching, sorting, and dynamic programming)
# - Art and Architecture (in the golden ratio)
# - Finance (for stock market predictions using Fibonacci retracement)

import time

def fibonacci_recursive(n):
    """Standard recursive Fibonacci (inefficient for large n)."""
    # Base cases for the sequence
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    # Recursive step: sum of two previous Fibonacci numbers
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo={}):
    """Optimized recursive Fibonacci using memoization (stores past results)."""
    # Check if the result for n is already in the memo dictionary (to avoid redundant calculations)
    if n in memo:
        return memo[n]
    
    # Base cases for the sequence
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    
    # Store the result of the current Fibonacci calculation in the memo dictionary
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def fibonacci_iterative(n):
    """Efficient iterative Fibonacci (best for large numbers)."""
    # Base cases for the sequence
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    
    # Use two variables to hold the two previous numbers
    prev, curr = 0, 1
    # Loop through and calculate Fibonacci iteratively
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def measure_time(func, n):
    """Measures execution time of a Fibonacci function."""
    start_time = time.time()  # Start time measurement
    result = func(n)  # Run the Fibonacci function
    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    return result, elapsed_time

if __name__ == "__main__":
    n = 35  # Large Fibonacci number to compare efficiency

    # Measure times for each approach
    _, recursive_time = measure_time(fibonacci_recursive, 30)  # Limited to 30 due to slowness
    memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
    iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

    # Output results for comparison
    print(f"Recursive fib(30) computed (Time: {recursive_time:.4f} sec) ❌ (Too slow for large n!)")
    print(f"Memoized fib({n}) = {memoized_result} (Time: {memoized_time:.6f} sec) ✅")
    print(f"Iterative fib({n}) = {iterative_result} (Time: {iterative_time:.6f} sec) ✅")

    # Insights
    print("\n🚀 **Key Insights:**")
    print("- ❌ Regular recursion is painfully slow for large `n`.")
    print("- ✅ Memoization speeds it up **1000x** by avoiding redundant calculations.")
    print("- ⚡ Iteration remains the **fastest & most memory-efficient** choice.")
