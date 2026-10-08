# অধ্যায় ৫, অনুশীলনী ৩

smallest = int(input("Enter number: "))
for _ in range(4):
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
print(f"The smallest number was: {smallest}")
