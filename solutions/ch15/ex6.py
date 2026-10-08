# অধ্যায় ১৫, অনুশীলনী ৬

n = int(input("Enter n: "))
fibs = []
a, b = 1, 1
for _ in range(n):
    fibs.append(a)
    a, b = b, a + b
print(fibs)
