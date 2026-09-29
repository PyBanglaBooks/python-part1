def is_prime2(n):
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

print(is_prime2(77), is_prime2(50), is_prime2(53))
