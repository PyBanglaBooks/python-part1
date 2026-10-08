# অধ্যায় ১২, অনুশীলনী ৫

phonebook = {}
while True:
    name = input("Name (q to quit): ")
    if name == "q":
        break
    number = input("Phone number: ")
    phonebook[name] = number

for name, number in phonebook.items():
    print(f"{name}: {number}")
