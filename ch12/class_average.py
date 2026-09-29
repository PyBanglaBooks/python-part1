classroom = [
    {"name": "Rahim", "marks": 85},
    {"name": "Karim", "marks": 78},
    {"name": "Nusrat", "marks": 92},
]

total = 0
for student in classroom:
    total += student["marks"]

average = total / len(classroom)
print(f"Class average: {average}")
