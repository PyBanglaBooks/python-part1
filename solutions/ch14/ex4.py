# অধ্যায় ১৪, অনুশীলনী ৪

FILENAME = "phonebook.txt"

phonebook = {}
try:
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            name, number = line.strip().split(",")
            phonebook[name] = number
except FileNotFoundError:
    print("Starting a new phonebook.")

while True:
    print("1. Add a number")
    print("2. Find a number")
    print("3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        phonebook[name] = number
    elif choice == "2":
        name = input("Name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Not found.")
    elif choice == "3":
        break
    else:
        print("Please choose 1, 2 or 3.")

with open(FILENAME, "w", encoding="utf-8") as f:
    for name, number in phonebook.items():
        f.write(f"{name},{number}\n")
print("Saved.")
