# অধ্যায় ৬, অনুশীলনী ২

while True:
    password = input("Enter a password: ")
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    if len(password) >= 6 and has_digit:
        break
    print("At least 6 characters and one digit, please.")

print("Password accepted.")
