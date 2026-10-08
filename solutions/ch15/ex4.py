# অধ্যায় ১৫, অনুশীলনী ৪

words = ["Apple", "Banana", "Apple", "Apple", "Orange"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

best = None
for word, count in counts.items():
    if best is None or count > counts[best]:
        best = word

print(f"{best} ({counts[best]} times)")
