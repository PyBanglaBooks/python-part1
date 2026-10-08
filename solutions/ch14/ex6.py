# অধ্যায় ১৪, অনুশীলনী ৬

results = []
for _ in range(5):
    name = input("Name: ")
    score = int(input("Score: "))
    results.append((score, name))

results.sort()
results.reverse()
print("Top 3:")
for score, name in results[:3]:
    print(f"{name} ({score})")
