text = "I love Bangladesh"
vowel_count = 0
for letter in text:
    if letter in "aeiou":
        vowel_count += 1
print(f"I found {vowel_count} vowels.")
