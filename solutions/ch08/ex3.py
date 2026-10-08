# অধ্যায় ৮, অনুশীলনী ৩

text = input("Enter a string: ")
upper = ""
lower = ""
digits = ""
others = ""
for char in text:
    if char.isupper():
        upper += char
    elif char.islower():
        lower += char
    elif char.isdigit():
        digits += char
    else:
        others += char
print(upper)
print(lower)
print(digits)
print(others)
