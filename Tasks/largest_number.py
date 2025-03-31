# largest_number.py 
# Written By Gower Campbell

# Learning Objectives: 
# - Understand how to solve problems using recursion.
# - Write recursive functions with proper base cases and recursive calls.
# - Avoid using loops or built-in functions like max() to solve the problem.

def largest_number(numbers):
    # My Base case:
    if len(numbers) == 1:
        return numbers[0]
    
    # Recursive case:
    rest_largest = largest_number(numbers[1:])
    if numbers[0] > rest_largest:
        return numbers[0]  # Return the first element if it's larger
    else:
        return rest_largest  # Otherwise, return the largest from the rest
    

# Example usage
largest1 = largest_number([1, 4, 5, 3])
largest2 = largest_number([3, 1, 6, 8, 2, 4, 5])
print(largest1)  # Output: 5
print(largest2)  # Output: 8

# <----- Reflections ---->
# I learned how to find the largest number in a list using recursion. 
# By breaking the problem into smaller subproblems, I compared the first 
# element with the largest number in the remaining list. This helped me 
# understand how recursion simplifies problem-solving by reducing the problem 
# size with each call. 

"""
<----- Bibliography ---->
- Python Documentation: 
https://docs.python.org/3/
- Youtube Find The Maximum Number In A List Without Using max() 
https://www.youtube.com/watch?v=RNHhgJcDjI8
- Pynote Python Recursion
https://pynote.readthedocs.io/en/latest/FunctionInPy/Recursion.html
- GeeksforGeeks Recursion Guide: 
https://www.geeksforgeeks.org/recursion/
"""
