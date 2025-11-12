import datetime

def show_categories(categories):
    print("\n--- Welcome to Family Restaurant ---\n")
    print("Please choose a food category:\n")
    for name, number in categories.items():
        print(f"{number}. {name}")
    print("-" * 35)


def show_menu(menu_dict, title):
    print(f"\n--- {title} MENU ---\n")
    for name, (num, price) in menu_dict.items():
        if num != 0:
            print(f"{num}. {name} - Rs-/{price}")
        else:
            print(f"{num}. {name}")
    print("-" * 35)
    

def handle_menu(menu_dict, title, order_list, total_bill):
    while True:
        show_menu(menu_dict, title)
        food_choice = input("Select a food item (number only): ").strip()

        if not food_choice.isdigit():
            print("\n❌ Please enter a valid number!\n")
            continue

        food_choice = int(food_choice)

        if food_choice == 0:
            print("\n↩ Returning to main menu...\n")
            break

        selected_food = None
        selected_price = 0
        for item, (num, price) in menu_dict.items():
            if num == food_choice:
                selected_food = item
                selected_price = price
                break

        if selected_food:
            quantity = input(f"Enter quantity for {selected_food}: ").strip()

            if not quantity.isdigit() or int(quantity) <= 0:
                print("\n❌ Please enter a valid positive quantity!\n")
                continue

            quantity = int(quantity)
            total_price = selected_price * quantity
            total_bill += total_price
            order_list.append((selected_food, quantity, total_price))

            print(f"\n✅ Added {quantity} x {selected_food} (Rs-/{total_price}) to your cart!\n")
        else:
            print("\n❌ Invalid option. Try again.\n")

    return total_bill
