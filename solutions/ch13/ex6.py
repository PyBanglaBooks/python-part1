# অধ্যায় ১৩, অনুশীলনী ৬

filename = input("Which file do you want to open? ")
try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("দুঃখিত, ফাইলটি পাওয়া যায়নি।")
