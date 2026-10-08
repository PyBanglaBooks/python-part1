n = int(input("Enter n: "))
fib_x = 1
fib_next = 1
for _ in range(n - 2):
    fib_temp = fib_x + fib_next
    fib_x = fib_next
    fib_next = fib_temp
print(fib_next)
