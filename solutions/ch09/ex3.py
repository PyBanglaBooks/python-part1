# অধ্যায় ৯, অনুশীলনী ৩

scores = [45, 88, 12, 99, 53, 24]

highest = scores[0]
lowest = scores[0]
total = 0
for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    total += score

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {total / len(scores)}")
