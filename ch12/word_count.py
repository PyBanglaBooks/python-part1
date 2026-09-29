text = "apple banana apple orange apple banana"
counts = {}
for word in text.split():
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)
