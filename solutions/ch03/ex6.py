# অধ্যায় ৩, অনুশীলনী ৬

a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))

if a + b > c and a + c > b and b + c > a:
    print("A triangle can be made.")
else:
    print("A triangle cannot be made.")
