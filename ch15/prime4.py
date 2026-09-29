import math

def is_prime4(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(math.sqrt(n)) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

primes = [n for n in range(1, 50) if is_prime4(n)]
print(primes)
