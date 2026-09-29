numbers = [10, 20, 4, 4, 20, 5]

first = None
second = None
for n in numbers:
    if first is None or n > first:
        second = first
        first = n
    elif n != first and (second is None or n > second):
        second = n

print(f"Second largest is: {second}")
