# factorial.py - Gower Campbell  
# Exploring recursion vs iteration for calculating factorials.  

import time  

def factorial_recursive(n):  
    """Computes factorial recursively."""  
    if n == 0:  # Base case  
        return 1  
    return n * factorial_recursive(n - 1)  # Recursive case  

def factorial_iterative(n):  
    """Computes factorial iteratively."""  
    result = 1  
    for i in range(1, n + 1):  
        result *= i  
    return result  

if __name__ == "__main__":  
    n = 10  # Test value  

    # Measure recursive execution time  
    start_time = time.time()  
    recursive_result = factorial_recursive(n)  
    recursive_time = time.time() - start_time  

    # Measure iterative execution time  
    start_time = time.time()  
    iterative_result = factorial_iterative(n)  
    iterative_time = time.time() - start_time  

    # Print results  
    print(f"Recursive {n}! = {recursive_result} (Time: {recursive_time:.8f} sec)")  
    print(f"Iterative {n}! = {iterative_result} (Time: {iterative_time:.8f} sec)")  

    # Observations  
    print("\nRecursion feels elegant ✨, but iteration is generally faster and avoids stack overflow for large values!")  
