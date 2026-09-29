def is_prime1(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} is divisible by {x}")
            prime = False
    return prime

while True:
    number = int(input("Please enter a number (enter 0 to exit): "))
    if number == 0:
        break
    if is_prime1(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
