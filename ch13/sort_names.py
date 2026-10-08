with open("names.txt", "w", encoding="utf-8") as f:
    for name in ["Rahim", "Sumon", "Karim", "Tania"]:
        f.write(name + "\n")

names = []
with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        names.append(line.strip())

names.sort()
print(names)
