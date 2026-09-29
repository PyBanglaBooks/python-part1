import random

number = random.randint(1, 1000)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number (between 1 and 1000): "))
    except ValueError:
        print("Please enter a number.")
        continue
    attempts += 1
    if guess == number:
        print("Yes, your guess is correct!")
        break
    if guess > number:
        print("Incorrect! Please try to guess a smaller number.")
    else:
        print("Incorrect! Please try to guess a larger number.")

print(f"You tried {attempts} times to find the correct number.")
