# অধ্যায় ১৫, অনুশীলনী ১

import math

def is_prime(n):
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

n1 = int(input("n1: "))
n2 = int(input("n2: "))
for n in range(n1, n2 + 1):
    if is_prime(n):
        print(n)
