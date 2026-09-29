target = 7
ways = 0
for d1 in range(1, 7):
    for d2 in range(1, 7):
        if d1 + d2 == target:
            print(f"Found one: {d1} + {d2}")
            ways += 1
print(f"Total ways to make {target}: {ways}")
