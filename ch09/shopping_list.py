shopping_list = []

while True:
    item = input("Add an item (or 'done' to finish): ")
    if item == "done":
        break
    shopping_list.append(item)

shopping_list.sort()
print("Your shopping list:")
for item in shopping_list:
    print(f"- {item}")
