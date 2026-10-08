# অধ্যায় ১৪, অনুশীলনী ২

import random

counts = {}
for _ in range(600):
    face = random.randint(1, 6)
    counts[face] = counts.get(face, 0) + 1

for face in range(1, 7):
    print(f"{face}: {counts.get(face, 0)}")
