# অধ্যায় ৮, অনুশীলনী ৫

word = input("Enter a word: ")
word = word.lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
