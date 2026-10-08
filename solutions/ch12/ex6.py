# অধ্যায় ১২, অনুশীলনী ৬

users = {"rahim": "apple123", "tania": "mango456"}

name = input("Username: ")
password = input("Password: ")

if name in users and users[name] == password:
    print("Welcome!")
else:
    print("Wrong username or password.")
