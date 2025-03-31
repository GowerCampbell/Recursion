# sum_recursion.py 
# Written By Gower Campbell

# Learning Objectives: 
# - Understand the basics of recursion and how it differs from iteration.
# - Write recursive functions with proper base cases and recursive calls.
# - Visualize the call stack and how a base case stops recursion.

def adding_up_to(numbers, index):
    # Base case: if the index is 0, return the first element
    if index == 0:
        return numbers[0]
    # Recursive case: add the current number to the sum of the previous numbers
    return numbers[index] + adding_up_to(numbers, index - 1)


# Example usage
sum_total1 = adding_up_to([1, 4, 5, 3, 12, 16], 4)
sum_total2 = adding_up_to([4, 3, 1, 5], 1)
print(sum_total1)  # Output: 25
print(sum_total2)  # Output: 7

# <----- Reflections ---->
# I learned how to sum elements in a list by writing a recursive function that
#  calls itself, stacking values until the base case is reached. This helped 
# me understand how base and recursive cases work together to solve problems.
#  I also visualized the call stack, which clarified how recursion builds
#  and resolves. Moving forward, I plan to practice more recursive problems
#  and explore optimizations like memoization to deepen my understanding. 

"""
<----- Bibliography ---->
- Python Documentation: 
https://docs.python.org/3/
- Pynote Python Recursion
https://pynote.readthedocs.io/en/latest/FunctionInPy/Recursion.html
- GeeksforGeeks Recursion Guide: 
https://www.geeksforgeeks.org/recursion/
"""
