# অধ্যায় ৮, অনুশীলনী ৪

s = input("Enter a string: ")
result = ""
for i in range(0, len(s), 2):
    result += s[i:i + 2][::-1]
print(result)
