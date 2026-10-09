sentence = "The dog barked. The dog ran, and the cat ran!"
unique = set()
for word in sentence.lower().split():
    unique.add(word.strip(".,!?"))
print(f"{len(unique)} unique words")
print(sorted(unique))
