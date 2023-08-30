print("Available Items:")
print("1. Apple")
print("2. Bread")
print("3. Milk")
print("4. Eggs")
print("5. Potato Chips")
print('6. Banana')

items = {
    "1" : {
        "Item_name" : "Apple",
        "Price" : 20
    },
    "2" : {
        "Item_name" : "Bread",
        "Price" : 25
    },
    "3" : {
        "Item_name" : "Milk",
        "Price" : 50
    },
    "4" : {
        "Item_name" : "Egg",
        "Price" : 12
    },
    "5" : {
        "Item_name" : "Potato Chips",
        "Price" : 10
    },
    "6" : {
        "Item_name" : "Banana",
        "Price" : 8
    }
}
cart = {}
while True:
    item_no = input("Add item to cart(0 to check out): ")

    if item_no == "0":
        break

    if item_no in items :
        item_quantity = int(input("Please input Quantity: "))
        if item_quantity > 0:
            item_price = items[item_no]["Price"]
            net_price = item_price * item_quantity
            cart[items[item_no]["Item_name"]] = {
                "Quantity" : item_quantity,
                "Item Price" : net_price
            }
        else:
            print("\033[91mINVALID QUANTITY\033[0m")
    else :
        print("\033[91mINVALID INPUT\033[0m")

total_price = 0
print("========================INVOICE========================")
print("Your Order List: ")
for item_name, item_data in cart.items():
    total_price += item_data["Item Price"]
    print(f"For {item_data['Quantity']} {item_name} = {item_data['Item Price']}")
print("=======================================================")
print(f"Your total payable amount is: {total_price}")