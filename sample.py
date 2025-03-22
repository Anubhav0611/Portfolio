def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", add(x, y))
    elif operation == "-":
        print("Result:", subtract(x, y))
    elif operation == "*":
        print("Result:", multiply(x, y))
    elif operation == "/":
        try:
            print("Result:", divide(x, y))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operation!")
