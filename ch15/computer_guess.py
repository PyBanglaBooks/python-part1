import random

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000

while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"My guess is {guess}")
    if guess == number:
        print("Yes, my guess is correct!")
        break
    if guess > number:
        high = guess - 1
    else:
        low = guess + 1

print(f"I tried {attempts} times to find the correct number.")
