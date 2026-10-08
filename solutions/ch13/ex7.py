# অধ্যায় ১৩, অনুশীলনী ৭

countries = ["Afghanistan", "Argentina", "Australia", "Bangladesh",
             "Bhutan", "Brazil", "Canada", "China", "India", "Nepal"]

with open("countries.txt", "w", encoding="utf-8") as f:
    for country in countries:
        f.write(country + "\n")

# group the names by their first letter
groups = {}
with open("countries.txt", "r", encoding="utf-8") as f:
    for line in f:
        country = line.strip()
        letter = country[0].lower()
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(country)

for letter, names in groups.items():
    with open(f"{letter}.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")
    print(f"{letter}.txt: {names}")
