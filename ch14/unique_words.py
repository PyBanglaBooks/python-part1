sentence = "The dog chased the cat and the dog barked"
words = sentence.lower().split()
unique = set(words)
print(f"{len(unique)} unique words")
print(sorted(unique))
