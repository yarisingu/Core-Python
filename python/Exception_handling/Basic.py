def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Unsupported operand types.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("End of divide_numbers function.")


# Example usage
divide_numbers(10, 2)       # Valid division
divide_numbers(10, 0)       # Division by zero
divide_numbers("10", "2")   # Unsupported operand types
divide_numbers(10, "2")     # Other exception

print("End of program.")
