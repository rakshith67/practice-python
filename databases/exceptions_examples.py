import sys


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def get_integer():
    try:
        number = int(input("Please enter the number "))
        return number
    except ValueError:
        print("Please enter valid number")
    except EOFError:
        sys.exit(0)
    finally:
        print("Finally block always executes")


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("Cannot calculate factorial for large numbers")

a = get_integer()
b = get_integer()

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Division by 0 not defined")
else:
    print("Division performed successfully")

print("Program Terminating")
