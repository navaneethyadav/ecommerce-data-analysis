def calculator():
    print("Simple Calculator")
    while True:
        print("\nSelect operation: +, -, *, /, or 'q' to quit")
        op = input("Operation: ")

        if op == 'q':
            print("Exiting...")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if op == '+':
            print("Result:", a + b)
        elif op == '-':
            print("Result:", a - b)
        elif op == '*':
            print("Result:", a * b)
        elif op == '/':
            print("Result:", a / b if b != 0 else "Error: Division by zero")
        else:
            print("Invalid operation!")

calculator()

