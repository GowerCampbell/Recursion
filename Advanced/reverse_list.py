# reverse_list.py - Gower Campbell  
# Reversing a list using recursion — feels like magic, but it's just smart stack usage!

def reverse_list(input_list):
    """
    Recursively reverses a list.
    
    How it works:
    - Base case: if the list is empty, return an empty list.
    - Recursive case: take the last element and place it at the front of the reversed rest.
    
    Think of it like peeling off the last item, flipping the rest, then stacking it all back up!
    """
    if not input_list:  # Base case: nothing to reverse
        return []
    
    # Recursive case:
    # 1. Take the last item from the list
    # 2. Recursively reverse the rest
    # 3. Combine them: last + reversed(rest)
    return [input_list[-1]] + reverse_list(input_list[:-1])

if __name__ == "__main__":
    # Test cases to see the function in action
    print(reverse_list([5, 6, 7, 8]))         # Output: [8, 7, 6, 5]
    print(reverse_list(["a", "b", "c"]))      # Output: ['c', 'b', 'a']
    print(reverse_list([]))                  # Output: []

    # Bonus insight:
    print("\n🧠 Think about it like this:")
    print("- You're peeling one item off the end each time.")
    print("- Once the list is empty, the pieces get stacked back up in reverse order.")
    print("- It’s all about how function calls stack and return in reverse!")

    print("\n🔥 Recursive list reversal feels magical — but now you know how the trick works!")
