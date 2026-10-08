# অধ্যায় ৮, অনুশীলনী ২

text = input("Enter a string: ")
result = ""
for char in text:
    if char in "aeiou":
        continue
    result += char
print(result)
