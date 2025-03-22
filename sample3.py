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

def exponentiate(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulus with zero!")
    return a % b

if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, **, %): ")

    try:
        if operation == "+":
            print("Result:", add(x, y))
        elif operation == "-":
            print("Result:", subtract(x, y))
        elif operation == "*":
            print("Result:", multiply(x, y))
        elif operation == "/":
            print("Result:", divide(x, y))
        elif operation == "**":
            print("Result:", exponentiate(x, y))
        elif operation == "%":
            print("Result:", modulus(x, y))
        else:
            print("Invalid operation!")
    except ValueError as e:
        print("Error:", e)
