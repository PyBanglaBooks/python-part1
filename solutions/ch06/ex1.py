# অধ্যায় ৬, অনুশীলনী ১

word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

if word == reversed_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
