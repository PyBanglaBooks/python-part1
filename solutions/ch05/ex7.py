# অধ্যায় ৫, অনুশীলনী ৭

import random

secret_number = random.randint(1, 20)
attempts = 0
won = False

print("I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")

while attempts < 5:
    guess = int(input("Make a guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You won in {attempts} guesses.")
        won = True
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if not won:
    print(f"Sorry, you lost. The number was {secret_number}.")
