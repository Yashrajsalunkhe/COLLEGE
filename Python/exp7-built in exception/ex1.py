def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide valid numeric values.")
    else:
        print(f"The result of {x} / {y} is: {result}")
    finally:
        print("This block always executes, regardless of whether an exception occurred or not.")

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Please enter valid numeric values for the numerator and denominator.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
