# Recursion vs Iteration in Python
# Written by Gower Campbell

"""
Recursion:
- Recursion occurs when a function calls itself.
- Used for problems that can be broken into smaller, simpler problems of the same type.
- Implements the 'divide and conquer' approach.
- Think of it as cooking: creating layers and ingredients (recursive calls) to build the final dish (solution).
- Requires careful handling of base cases to avoid infinite recursion.
- Simplicity, modularity, and flexibility are its strengths.

Iteration:
- Iteration uses loops (e.g., `for`, `while`) to repeat a block of code.
- Divided into:
  - Count-controlled iteration: Based on a fixed count or iteration variable.
  - Condition-controlled iteration: Based on a condition that determines the number of iterations.
- Offers better performance and predictable resource usage compared to recursion.
- Requires explicit variable state management.

Comparison:
- Both recursion and iteration achieve repetition but in different ways.
- Recursion solves problems intuitively and naturally, avoiding explicit state management.
- Iteration gives direct control over program flow and is more memory-efficient.
- Recursion is more memory-intensive and slower but offers elegance in solving certain problems.

Examples of Recursive and Iterative Approaches:
1. Factorial
2. Fibonacci Sequence
3. Tree and Graph Traversals
"""

# Factorial Calculation

# Recursive Approach
def factorial_recursive(num):
    """
    Calculate factorial recursively.
    Base Case: If num == 0, return 1.
    Recursive Case: n! = n * (n - 1)!
    """
    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num - 1)

# Iterative Approach
def factorial_iterative(num):
    """
    Calculate factorial iteratively.
    Multiply numbers from 1 to num using a loop.
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Test Factorial Functions
print("Factorial Results:")
print("Recursive:", factorial_recursive(5))  # Output: 120
print("Iterative:", factorial_iterative(5))  # Output: 120

"""
Additional Details for Factorial Approaches:
Recursive:
- Recursive factorial calls itself repeatedly, reducing the number by 1 each time.
- Example for 4!:
  factorial_recursive(4) = 4 * factorial_recursive(3)
  factorial_recursive(3) = 3 * factorial_recursive(2)
  factorial_recursive(2) = 2 * factorial_recursive(1)
  factorial_recursive(1) = 1
  Answer = 4 * 3 * 2 * 1 = 24

Iterative:
- Uses a `for` loop to calculate factorial iteratively.
- Directly multiplies numbers from 1 to the given number.
- Example for 4!:
  Loop iterates through 1, 2, 3, 4
  Result = 1 * 2 * 3 * 4 = 24
"""

# Fibonacci Sequence

# Iterative Approach
def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number iteratively.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_prev, fib_curr = 0, 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next

    return fib_curr

# Recursive Approach
def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number recursively.
    Base Case: fib(0) = 0, fib(1) = 1.
    Recursive Case: fib(n) = fib(n - 1) + fib(n - 2).
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

"""
Additional Details for Fibonacci Approaches:
Recursive:
- Recursive Fibonacci repeatedly calls itself for `n - 1` and `n - 2` until reaching base cases (0 or 1).
- Example for fib(4):
  fibonacci_recursive(4) = fibonacci_recursive(3) + fibonacci_recursive(2)
  fibonacci_recursive(3) = fibonacci_recursive(2) + fibonacci_recursive(1)
  fibonacci_recursive(2) = fibonacci_recursive(1) + fibonacci_recursive(0)
  Result = (1 + 0 + 1) + (1 + 0) = 3

Iterative:
- Uses a loop to calculate Fibonacci numbers step by step.
- Example for fib(4):
  fib_prev = 0, fib_curr = 1
  Iteration 1: fib_next = 1, fib_prev = 1, fib_curr = 1
  Iteration 2: fib_next = 2, fib_prev = 1, fib_curr = 2
  Iteration 3: fib_next = 3, fib_prev = 2, fib_curr = 3
  Result = 3
"""

# Test Fibonacci Functions
def test_fibonacci():
    print("\nTesting Fibonacci Functions:")

    # Base Cases
    print("fibonacci_recursive(0):", fibonacci_recursive(0))
    print("fibonacci_recursive(1):", fibonacci_recursive(1))

    # Step-by-step Explanation for fibonacci(4):
    print("\nStep-by-step breakdown for fibonacci(4):")
    print("fibonacci(4) = fibonacci(3) + fibonacci(2)")
    print("fibonacci(3) = fibonacci(2) + fibonacci(1)")
    print("fibonacci(2) = fibonacci(1) + fibonacci(0)")
    print("fibonacci(4) = (fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0))")
    print("fibonacci(4) = (1 + 0 + 1) + (1 + 0) = 3")

    # Additional Tests
    print("\nAdditional Test Cases:")
    print("Iterative:", fibonacci_iterative(6))  # Output: 8
    print("Recursive:", fibonacci_recursive(6))  # Output: 8

if __name__ == "__main__":
    # Test Factorial
    print("\nFactorial Results:")
    print("Recursive:", factorial_recursive(6))
    print("Iterative:", factorial_iterative(6))

    # Test Fibonacci
    test_fibonacci()

# Recursion Tutorial
# Written By Gower Campbell

# Recursion: A Handy Programming Tool

# Recursive programming "THINK RECURSIVELY" encourages breaking problems into smaller, manageable chunks:
# Compact and easy-to-understand code with fewer variables.

# Both recursion and iteration (loops) achieve repetition:
# - Loops specify repetitive structures explicitly.
# - Recursion uses continuous function calls for repetition.

# Guidelines:
# - Use recursion for compact, intuitive, or natural solutions.
# - Use iteration when limited memory and faster processing are required.

# Visualize recursion using "Russian dolls":
# - Recursion stops at the smallest doll—called the "base case."
# - The base case is the smallest or last variable in a data structure that stops the recursion.

# A recursive function calls itself until a specified condition (base case) is met, and a result is returned.

# Example 1: Cutting Cake
# The `cut_cake` function demonstrates a recursive approach to doubling slices of cake until the number of slices
# is sufficient for the number of friends.
def cut_cake(number_of_friends, number_of_slices):
    # Double the number of slices
    number_of_slices *= 2

    # Check if there are enough slices for everyone
    if number_of_slices >= number_of_friends:  # Base case
        return number_of_slices
    else:
        # If not, cut the cake again
        return cut_cake(number_of_friends, number_of_slices)

print(cut_cake(11, 1))  # Output: 16

# Explanation:
# - The function takes the number of friends (11) and the initial number of slices (1).
# - Slices are repeatedly doubled until they meet or exceed the number of friends.

# Example 2: Factorials & Recursion
# Factorials describe the operation of multiplying a number by all positive integers less than or equal to itself.
# For example:
# - 4! = 4 * 3 * 2 * 1
# - 0! = 1 (by definition)

def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n - 1)!
        return n * factorial(n - 1)

print(f"The factorial of 4 is {factorial(4)}")  # Output: The factorial of 4 is 24

# Explanation:
# - If n = 0, return 1 (base case).
# - For n > 0, multiply n by the factorial of (n - 1).
# - The function keeps calling itself until n reaches 0.

# Recursion in Python
# Python has a maximum recursion depth limit due to memory constraints.
# Each recursive call creates a new local namespace, increasing memory usage.

# By default, Python limits recursion depth to 1000 calls.
from sys import getrecursionlimit, setrecursionlimit

print(getrecursionlimit())  # Default: 1000

# You can change the recursion limit:
setrecursionlimit(2000)
print(getrecursionlimit())  # New limit: 2000

# Note: Increasing the recursion limit can lead to memory overflow if not used carefully.

# Example: A function without a base case would cause a RecursionError.
# Uncommenting the code below will cause a crash due to exceeding the recursion depth.
#
def infinite_recursion():
    return infinite_recursion()

# infinite_recursion()  # Uncomment to test (will raise RecursionError)

    """Factorial Example
    4! = 4
    """

def fact(n):
    if n == 1: # base case
        return 1
    else: 
        n * fact(n - 1)

print(fact(4))

"""
# Conclusion & Recap
The base case is where the function returns a value without making further recursive calls. 
Recursion is valued for its simplicity and elegance, enabling compact, understandable, 
and intuitive code that avoids explicit state management.Iteration, on the other hand,
excels in situations where limited memory and faster processing are required. 
It provides more direct control over the flow of execution, making it ideal 
for performance-critical tasks or when managing large inputs.
"""
