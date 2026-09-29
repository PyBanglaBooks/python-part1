def is_prime1(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divisible by", x)
            prime = False
    return prime

while True:
    number = int(input("Please enter a number (enter 0 to exit): "))
    if number == 0:
        break
    if is_prime1(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
