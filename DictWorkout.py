product_list = {"pen": 10, "pencil": 20}

def order(item, qty):
    if product_list.get(item):
        if product_list.get(item) >= qty:
            print(f"Your order {item} with quantity {qty} is placed sucessfully.!")
            product_list.update({item: product_list.get(item) - qty})
        else:
            print(f"Sorry! We have low quantity {qty} for the product of {item}")
    else:
        print(f"The given item {item} not avaible. The current product list is below.")
        i = 1
        for product,quantity in product_list.items():
            print(f"{i}. {product} - {quantity}")
            i+=1

order("mikl",10)
order("pen",9)

for product,quantity in product_list.items():
    print(f"{product} - {quantity}")

order("pen",2)
order("pencil",20)


for product,quantity in product_list.items():
    print(f"{product} - {quantity}")

order("pen",1)

for product,quantity in product_list.items():
    print(f"{product} - {quantity}")