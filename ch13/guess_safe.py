import random

secret_number = random.randint(1, 20)
attempts = 0
print("I am thinking of a number between 1 and 20.")

while True:
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please type a number.")
        continue
    attempts += 1
    if guess == secret_number:
        print(f"Correct! You won in {attempts} guesses.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
