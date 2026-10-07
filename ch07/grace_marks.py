def add_grace(marks):
    marks = marks + 5
    print(f"Inside the function: {marks}")

marks = 80
add_grace(marks)
print(f"Outside the function: {marks}")
