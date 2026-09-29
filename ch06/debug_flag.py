DEBUG = True    # বাড়তি লেখা লুকাতে চাইলে False করে দিতে হবে

x = 0
limit = 3
while x < limit:
    if DEBUG:
        print(f"DEBUG: x is {x}")
    x += 1
print("Done!")
