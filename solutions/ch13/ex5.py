# অধ্যায় ১৩, অনুশীলনী ৫

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print(f"{a} / {b} = {a / b}")
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
