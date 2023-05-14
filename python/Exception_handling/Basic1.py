def calculate_square(n):
    try:
        square = n ** 2
        print(f"The square of {n} is: {square}")
    except TypeError:
        print("Error: Invalid input. Please provide a numeric value.")

# Example usage
calculate_square(5)     # Valid input
calculate_square("hello")   # TypeError: Invalid input
calculate_square([1, 2, 3]) # TypeError: Invalid input
