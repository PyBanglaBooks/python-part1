def is_even(n):
    return n % 2 == 0

for i in range(1, 7):
    if is_even(i):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
