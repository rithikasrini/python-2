def display_dictionary(grocery):
    for item, details in grocery.items():
        print(f"{item}:")
        print(f"  Quantity: {details['quantity']}")
        print(f"  Price: {details['price']}\n")

def update_quantity(grocery, item, quantity):
    if item in grocery:
        grocery[item]['quantity'] += quantity
    else:
        print("Item not found!")

def update_price(grocery, item, price):
    if item in grocery:
        grocery[item]['price'] = price
    else:
        print("Item not found!")

def add_new_item(grocery, item, quantity, price):
    grocery[item] = {'quantity': quantity, 'price': price}
def main():
    grocery = {
        "Cornflakes": {"quantity": 15, "price": 100},
        "Muesli": {"quantity": 14, "price": 150},
        "Oats": {"quantity": 10, "price": 80},
        "Wheat Flakes": {"quantity": 5, "price": 75},
        "Granola": {"quantity": 8, "price": 125}
    }

    display_dictionary(grocery)

    print("What do you want to do?")
    print("1. Add additional quantity of cereals")
    print("2. Update the price of the grocery")
    print("3. Add new item")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the grocery item name: ")
        quantity = int(input("Enter the quantity of the item to be added: "))
        update_quantity(grocery, item, quantity)
    elif choice == 2:
        item = input("Enter the grocery item name: ")
        price = int(input("Enter the new price of the item: "))
        update_price(grocery, item, price)
    elif choice == 3:
        item = input("Enter the new grocery item name: ")
        quantity = int(input("Enter the quantity of the new item: "))
        price = int(input("Enter the price of the new item: "))
        add_new_item(grocery, item, quantity, price)
    else:
        print("Invalid choice!")

    print("\nItem details after updating:\n")
    display_dictionary(grocery)


main()
