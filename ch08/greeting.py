import turtle

name = turtle.textinput("name", "What is your name?")
name = name.strip().lower()

if name.startswith("mr."):
    print("Hello Sir, how are you?")
elif name.startswith("mrs.") or name.startswith("ms."):
    print("Hello Madam, how are you?")
else:
    print(f"Hi {name.capitalize()}! How are you?")

turtle.exitonclick()
