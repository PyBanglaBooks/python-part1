def test_fnc(li):
    li[0] = 10

my_list = [1, 2, 3, 4]
print(f"before function call {my_list}")
test_fnc(my_list)
print(f"after function call {my_list}")
