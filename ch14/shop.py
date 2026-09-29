inventory = {"pen": 10, "notebook": 5, "eraser": 0}

while True:
    item = input("What do you want to buy? (type 'done' to finish): ")
    item = item.strip().lower()
    if item == "done":
        break
    stock = inventory.get(item)
    if stock is None:
        print("Sorry, we do not sell that.")
    elif stock == 0:
        print("Sorry, it is out of stock.")
    else:
        inventory[item] = stock - 1
        print(f"Here is your {item}.")

print("Stock left:")
for item, count in inventory.items():
    print(f"{item}: {count}")
