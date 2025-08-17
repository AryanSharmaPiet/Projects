from datetime import datetime

menu = {
    "pasta": 100,
    "pizza": 120,
    "coffee": 85,
    "sandwich": 55,
    "pav bhaji": 100,
    "chips": 20,
    "chocolate": 40
}

order = {}
TAX_RATE = 0.05

def show_menu():
    print("\n---- MENU ----")
    for item, price in menu.items():
        print(f"{item.title():<12} : ₹{price}")
    print("--------------\n")

def add_to_order(item, qty):
    if item in menu:
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        print(f"{qty} x {item.title()} added to your order.")
    else:
        print("Item not found in menu.")

def generate_bill():
    print("\n----- BILL -----")
    total = 0
    for item, qty in order.items():
        price = menu[item] * qty
        print(f"{item.title():<12} x {qty:<3} = ₹{price}")
        total += price

    tax = total * TAX_RATE
    final_amount = total + tax

    print("----------------")
    print(f"Subtotal      : ₹{total}")
    print(f"GST (5%)      : ₹{round(tax,2)}")
    print(f"Total Amount  : ₹{round(final_amount,2)}")
    print("----------------")

    with open("receipt.txt", "w") as f:
        f.write("----- RECEIPT -----\n")
        f.write(f"Date: {datetime.now()}\n\n")
        for item, qty in order.items():
            f.write(f"{item.title()} x {qty} = ₹{menu[item]*qty}\n")
        f.write(f"\nSubtotal: ₹{total}\nGST (5%): ₹{round(tax,2)}\n")
        f.write(f"Total: ₹{round(final_amount,2)}\n")
    print("Receipt saved as 'receipt.txt'")

print("Welcome to Python Restaurant!")
choice = input("Do you want to see the menu? (yes/no): ").lower()
if choice == "yes":
    show_menu()

while True:
    inp = input("Do you want to order? (yes/no): ").lower()
    if inp == "yes":
        item = input("Enter item name: ").lower()
        qty = int(input("Enter quantity: "))
        add_to_order(item, qty)
    elif inp == "no":
        if order:
            generate_bill()
        print("Thanks for visiting!")
        break
    else:
        print("Please enter yes or no.")