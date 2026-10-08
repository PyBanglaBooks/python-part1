# অধ্যায় ১৫, অনুশীলনী ৫

n = int(input("Enter a positive integer: "))

original = n
reversed_n = 0
while n > 0:
    reversed_n = reversed_n * 10 + n % 10
    n //= 10

if original == reversed_n:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")
