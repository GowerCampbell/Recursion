# sum_of_digits.py - Gower Campbell  
# Summing the digits of a number using recursion — perfect for breaking numbers apart!

def sum_of_digits(n):
    """
    Recursively sums the digits of a number.

    How it works:
    - Base case: if the number is a single digit (less than 10), just return it.
    - Recursive case:
        - Add the last digit (n % 10) to the sum of the digits of the rest of the number (n // 10).
    
    Example: sum_of_digits(456)
      → 6 + sum_of_digits(45)
      → 6 + 5 + sum_of_digits(4)
      → 6 + 5 + 4 = 15
    """
    if n < 10:
        return n  # Base case: only one digit left
    return (n % 10) + sum_of_digits(n // 10)  # Add last digit + recurse on the rest

if __name__ == "__main__":
    # Test the function with a few examples
    print(f"Sum of digits in 123 → {sum_of_digits(123)}")   # Output: 6
    print(f"Sum of digits in 456 → {sum_of_digits(456)}")   # Output: 15
    print(f"Sum of digits in 9999 → {sum_of_digits(9999)}") # Output: 36

    # Reflection
    print("\n🧠 Recursive Insight:")
    print("- We break the number into its last digit (using % 10), then work on the rest (using // 10).")
    print("- Recursion handles the shrinking naturally until we hit a single digit.")
    print("- This is one of those problems where recursion feels super intuitive!")

    print("\n✨ It’s like peeling off digits from right to left and adding them up as the calls return!")
