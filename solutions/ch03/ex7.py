# অধ্যায় ৩, অনুশীলনী ৭

num1 = float(input("First number: "))
op = input("Operator (+, -, *, /, //, %): ")
num2 = float(input("Second number: "))

if num2 == 0 and (op == "/" or op == "//" or op == "%"):
    print("Cannot divide by zero.")
elif op == "+":
    print(f"Result: {num1 + num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
elif op == "/":
    print(f"Result: {num1 / num2}")
elif op == "//":
    print(f"Result: {num1 // num2}")
elif op == "%":
    print(f"Result: {num1 % num2}")
else:
    print("Unknown operator.")
