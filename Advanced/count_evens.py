# count_evens.py - Gower Campbell  
# Counting even numbers in a list using recursion — a simple but satisfying challenge!

def count_evens(num_list):
    """
    Recursively counts the number of even integers in a list.
    
    Logic:
    - Base case: If the list is empty, return 0.
    - Recursive case: 
        - Check if the first element is even (divisible by 2)
        - Add 1 if it is, otherwise add 0
        - Recurse on the rest of the list
    """
    if not num_list:  # Base case: no more numbers to check
        return 0

    # Check the first number, then recurse on the rest
    is_even = 1 if num_list[0] % 2 == 0 else 0
    return is_even + count_evens(num_list[1:])

if __name__ == "__main__":
    # Test the function with a sample list
    test_list = [2, 1, 4, 5, 8]
    print(f"Even numbers in {test_list} → {count_evens(test_list)}")  # Output: 3

    # Reflection
    print("\n🧠 Recursive Insight:")
    print("- We slice the list one item at a time (num_list[1:]) and check if the first is even.")
    print("- This builds up a count as the call stack unwinds.")
    print("- It’s a clean and readable way to count, especially when loops aren’t allowed!")

    print("\n✅ Clean logic, clear recursion — and no need to track counters manually!")
