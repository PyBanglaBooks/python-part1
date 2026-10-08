# অধ্যায় ৭, অনুশীলনী ৪

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(find_max(3, 9, 5))
print(find_max(7, 2, 7))
print(find_max(-1, -5, -3))
