n = int(input("Enter a number: "))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n = n // 10
        count += 1

print(f"Number of digits: {count}")
