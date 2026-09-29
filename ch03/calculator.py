num1 = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))

if op == "+":
    print(f"Result: {num1 + num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Unknown operator.")
