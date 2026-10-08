# অধ্যায় ৯, অনুশীলনী ৪

numbers = [1, 2, 3, 4]

squares = []
for n in numbers:
    squares.append(n * n)
print(squares)

squares = [n * n for n in numbers]
print(squares)
