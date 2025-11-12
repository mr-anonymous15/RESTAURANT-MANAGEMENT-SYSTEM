# main.py
import datetime
from menu_data import categories, fast_food, desi_food, chinese_food, vegetarian_food, drinks
from menu_functions import show_categories, handle_menu

# --- MAIN PROGRAM LOOP ---
customer_name = input("Please enter your name: ").strip().title()
order_list = []
total_bill = 0

while True:
    show_categories(categories)
    choice = input("Enter your choice (number only): ").strip()

    if not choice.isdigit():
        print("\n❌ Please enter a valid number!\n")
        continue

    choice = int(choice)

    if choice == 0:
        now = datetime.datetime.now()
        print("\nThank you for visiting Family Restaurant! 🍽️")

        print("\n----- 🧾 ORDER SUMMARY -----")
        for item, qty, price in order_list:
            print(f"{item} x {qty} = Rs-/{price}")
        print("-----------------------------")
        print(f"TOTAL BILL: Rs-/{total_bill}")
        print(f"Date: {now.strftime('%d %b %Y, %I:%M %p')}")
        print("-----------------------------\n")

        with open("orders.txt", "a", encoding="utf-8") as file:
            file.write(f"Customer: {customer_name}\n")
            file.write(f"Date: {now.strftime('%d %b %Y, %I:%M %p')}\n")
            file.write("Items Ordered:\n")
            for item, qty, price in order_list:
                file.write(f"  - {item} x {qty} = Rs-/{price}\n")
            file.write(f"Total Bill: Rs-/{total_bill}\n")
            file.write(f"Thanks for ordering we are pleasure to serve you!\n")
            file.write("-" * 40 + "\n")

        print(f"💾 Order saved successfully!\n")
        print(f"🙏 Thank you, Mr/Mrs. {customer_name}! Hope to see you again ❤️\n")
        break

    # Match category and call menu handler
    if choice == 1:
        total_bill = handle_menu(fast_food, "FAST FOOD", order_list, total_bill)
    elif choice == 2:
        total_bill = handle_menu(desi_food, "DESI FOOD", order_list, total_bill)
    elif choice == 3:
        total_bill = handle_menu(chinese_food, "CHINESE FOOD", order_list, total_bill)
    elif choice == 4:
        total_bill = handle_menu(vegetarian_food, "VEGETARIAN FOOD", order_list, total_bill)
    elif choice == 5:
        total_bill = handle_menu(drinks, "DRINKS", order_list, total_bill)
    else:
        print("\n❌ Invalid category number. Try again.\n")
