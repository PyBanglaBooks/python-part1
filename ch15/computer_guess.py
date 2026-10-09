import random

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000
print(f"Secret number: {number}")

while True:
    guess = (low + high) // 2
    attempts += 1
    if guess == number:
        print(f"My guess is {guess}. Correct!")
        break
    if guess > number:
        print(f"My guess is {guess}. Too high!")
        high = guess - 1
    else:
        print(f"My guess is {guess}. Too low!")
        low = guess + 1

print(f"I tried {attempts} times to find the correct number.")
