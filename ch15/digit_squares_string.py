number_text = input("Enter a positive integer: ")
total = 0
for ch in number_text:
    digit = int(ch)
    total += digit ** 2
print(f"Sum of squares of digits: {total}")
