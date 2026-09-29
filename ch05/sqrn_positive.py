while True:
    n = int(input("Please enter a positive number (0 to exit): "))
    if n < 0:
        print("Only positive numbers are allowed. Please try again.")
        continue
    if n == 0:
        break
    print(f"Square of {n} is {n * n}")
