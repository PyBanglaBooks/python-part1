# অধ্যায় ১৩, অনুশীলনী ২

name = input("Name: ")
score = input("Score: ")
with open("scores.txt", "a", encoding="utf-8") as f:
    f.write(f"{name}: {score}\n")
