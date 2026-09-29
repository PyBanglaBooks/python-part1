with open("diary.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())
