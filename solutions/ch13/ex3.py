# অধ্যায় ১৩, অনুশীলনী ৩

best_name = ""
best_score = -1
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, score = line.strip().split(": ")
        score = int(score)
        if score > best_score:
            best_name = name
            best_score = score

print(f"Highest score: {best_name} ({best_score})")
