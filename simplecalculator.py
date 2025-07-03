def calculator():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operator.")

calculator()
