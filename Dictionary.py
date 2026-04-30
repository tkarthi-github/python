grocery_list = {"milk":5,"water": 10}
print(type(grocery_list))

# grocery_list.update({"milk": 10})

dup_grocery_list = {}

for item,qty in grocery_list.items():
    dup_grocery_list.update({item:qty*2})
    print(f"The Item {item} added with {qty*2} in the duplicate grocery list")
print(grocery_list)
print(dup_grocery_list)

# print(dup_grocery_list.keys())

for item in dup_grocery_list.keys():
    print(item)

for value in dup_grocery_list.values():
    print(value)

print(dup_grocery_list.pop("milk"))
print(dup_grocery_list.popitem())

dup_grocery_list.clear();
print(dup_grocery_list)