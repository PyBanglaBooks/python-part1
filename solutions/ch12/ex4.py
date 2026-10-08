# অধ্যায় ১২, অনুশীলনী ৪

sentence = input("Enter a sentence: ")
counts = {}
for char in sentence:
    counts[char] = counts.get(char, 0) + 1

for char, count in counts.items():
    print(f"'{char}': {count}")
