def factorial_iterative(n):
    """
    Calculate factorial of n using an iterative approach.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial of n using a recursive approach.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Test the functions
if __name__ == "__main__":
    test_values = [0, 1, 5, 10]
    print("Iterative factorial:")
    for val in test_values:
        print(f"{val}! = {factorial_iterative(val)}")

    print("\nRecursive factorial:")
    for val in test_values:
        print(f"{val}! = {factorial_recursive(val)}")
