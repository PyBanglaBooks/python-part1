try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you will be {age + 10}")
except ValueError:
    print("That is not a number! Please type digits only.")
