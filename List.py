shopping_card_items = []
print(shopping_card_items)
print(type(shopping_card_items))

for i in range(2,20,2):
    shopping_card_items.append(i)

# print(shopping_card_items)

# for i in range(1,20,2):
#     shopping_card_items.append(i)

print(shopping_card_items)

# print(shopping_card_items[0:10])
# print(shopping_card_items[10])

# for num in shopping_card_items:
#     print(num + 1)

index_lastitem = shopping_card_items.pop()
print(index_lastitem)
print(shopping_card_items)

shopping_card_items.insert(1,15)
print(shopping_card_items)

# shopping_card_items.sort(reverse=True)
# print(shopping_card_items)

shopping_card_items.reverse()
print(shopping_card_items)

length = len(shopping_card_items)
print(f"The length of List is -> {length}")

