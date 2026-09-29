text = input("Enter a word: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Reversed: {reversed_text}")
