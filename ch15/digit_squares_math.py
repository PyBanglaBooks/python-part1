n = int(input("Enter a positive integer: "))
total = 0
while n > 0:
    digit = n % 10
    total += digit ** 2
    n //= 10
print(f"Sum of squares of digits: {total}")
