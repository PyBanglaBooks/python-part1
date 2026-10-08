# অধ্যায় ৬, অনুশীলনী ৪

n = int(input("Enter a positive integer: "))
total = 0
while n > 0:
    total += n % 10
    n = n // 10
print(f"Sum of digits: {total}")
