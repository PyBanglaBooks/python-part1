# অধ্যায় ১২, অনুশীলনী ২

words = {"apple": "আপেল", "book": "বই", "water": "পানি", "sun": "সূর্য"}

word = input("Enter an English word: ").strip().lower()
if word in words:
    print(words[word])
else:
    print("দুঃখিত, শব্দটি জানা নেই।")
