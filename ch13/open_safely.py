try:
    with open("secret_plans.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Sorry, I could not find the file.")
