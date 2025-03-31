# sum_natural_numbers.py - Gower Campbell  
# Three ways to sum natural numbers: recursion, iteration, and a formula.

def sum_recursive(n):
    """
    Sums numbers from 1 to n using recursion.
    
    Recursion is elegant but can be slow for large values of n
    due to repeated function calls and memory usage.
    """
    if n == 0: 
        return 0  # Base case: sum of 0 is 0
    return n + sum_recursive(n - 1)  # Recursive case: sum current number with result of smaller problem

def sum_iterative(n):
    """
    Sums numbers from 1 to n using a loop (iteration).
    
    Iteration is typically faster than recursion and doesn't use 
    extra memory for function calls, making it better for larger n.
    """
    result = 0
    for i in range(n + 1):  # Loop from 0 to n (inclusive)
        result += i  # Add each number to the result
    return result

def sum_formula(n):
    """
    Sums numbers from 1 to n using the mathematical formula.
    
    Formula: n * (n + 1) // 2  
    This is a constant-time solution, making it the fastest approach.
    """
    return n * (n + 1) // 2  # The sum of the first n natural numbers: n(n+1)/2

if __name__ == "__main__":
    n = 6  # Test with a small number (you can try bigger numbers too!)
    
    # Compare the results of each approach:
    print(f"Recursive sum({n}) = {sum_recursive(n)}")  # Output: 21
    print(f"Iterative sum({n}) = {sum_iterative(n)}")  # Output: 21
    print(f"Formula sum({n}) = {sum_formula(n)}")  # Output: 21
    
    # Explanation of the approaches:
    print("\n💡 Insights:")
    print("- Recursion is elegant, but can be slow and memory-intensive for large values of `n`.")
    print("- Iteration is faster than recursion because it doesn't involve repeated function calls.")
    print("- The formula approach is **the fastest** because it computes the sum in constant time (O(1))!")
    print("\n⚡ **Formula wins for speed**, but recursion helped me 'think recursively' and understand problem breaking!")
