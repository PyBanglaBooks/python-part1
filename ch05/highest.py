print("Enter 3 numbers to see which is biggest.")
highest = int(input("Enter number: "))
for _ in range(2):
    num = int(input("Enter number: "))
    if num > highest:
        highest = num
print(f"The highest number was: {highest}")
