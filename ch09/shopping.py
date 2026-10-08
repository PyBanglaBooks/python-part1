def add_item(shopping, item):
    shopping.append(item)

shopping = ["rice", "egg"]
print(f"Before: {shopping}")
add_item(shopping, "milk")
print(f"After: {shopping}")
