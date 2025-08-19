def divide_numbers(a, b):
    try:
        c = a / b
        return f"Division: {c}"

    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Invalid input, please enter numbers."
    except Exception as e:
        return e


print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers("ten", 2))
