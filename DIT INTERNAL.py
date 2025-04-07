"""this program allows users to choose and order poke bowls."""

import os

"""list of menu items, this is also where custom orders are stored"""
poke_bowl_menu_items = [["1:", "Salmon", "Rice", "Avacado", "Corn", 22],["2:", "Tuna", "Rice", "Avacado", "Radish", 22],["3:", "Tofu", "Rice", "Radish", "Cucumber", 21],["4:", "Snapper", "Rice", "Corn", "Edamame", 25],["5:", "Chicken", "Rice", "Seaweed", "Carrot", 18]]

"""defines a function that prints out the full menu"""
def full_poke_bowl_menu():
    for poke_bowl_menu_item in poke_bowl_menu_items:
        print("------------------------------------")
        print(poke_bowl_menu_item[0], poke_bowl_menu_item[1], poke_bowl_menu_item[2], poke_bowl_menu_item[3], poke_bowl_menu_item[4], poke_bowl_menu_item[5])

""""defines a function that allows users to order pre-exisitng items"""
def order_preexisting_items():
    os.system("clear")
    for poke_bowl_menu_item in poke_bowl_menu_items:
        print("------------------------------------")
        print(poke_bowl_menu_item[0], poke_bowl_menu_item[1], poke_bowl_menu_item[2], poke_bowl_menu_item[3], poke_bowl_menu_item[4], poke_bowl_menu_item[5])

    user_order = int(input("\n\nWhat would you like to order?\n\n>"))

    while True:
        try:  
            if user_order == 1:
                print("1: | Salmon, Rice, Avacado, Corn, 22")
            elif user_order == 2:
                print("2: | Tuna, Rice, Avacado, Radish, 22")
            elif user_order == 3:
                print("3: |  Tofu, Rice, Radish, Cucumber, 21")
            elif user_order == 4:
                print("4: | Snapper, Rice, Corn, Edamame, 25")
            elif user_order == 5:
                print("5: | Chicken, Rice, Seaweed, Carrot, 18")

        except ValueError:
            print("please enter a valid choice")                       

        while True:
            try:
                user_menu_choice = input("\n- Would you like to order something else? (yes/no): \n\n>").lower()
                if user_menu_choice == "yes":
                    order_preexisting_items()
                elif user_menu_choice == "no":
                   return
            except:
                print("invalid input")
   
"""this define a function that allows the user to customise their order"""
def order_custom_item():
    poke_bowl_menu_items.append([])
    
    valid_user_protein = ["Salmon", "salmon", "Tuna", "tuna", "Snapper", "snapper", "Chicken", "chicken", "Tofu", "tofu"]
    valid_user_base = ["Rice", "rice", "Brown Rice", "brown rice"]
    valid_user_veg = ["Avacado", "Corn", "Cucumber", "Edamame", "Radish", "Carrot" "avacado", "corn", "cucumber", "edamame", "radish", "carrot"]

    while True:
        new_order_protein = input("\nPlease enter your choice of protein (Salmon, Tuna, Snapper, Chicken, Tofu)\n>").lower()

        if new_order_protein in valid_user_protein:
            poke_bowl_menu_items[-1].append(new_order_protein)
            break
        else:
            print("\n\nInvalid ingredient choice, please try again")
            continue

    while True:
        new_order_carb = input("\nWhat is your choice of base? (Rice, Brown Rice)\n>").lower()

        if new_order_carb in valid_user_base:
            poke_bowl_menu_items[-1].append(new_order_carb)
            break
        else:
            print("\n\nInvalid ingredient choice, please try again")
            continue

    while True:
        new_order_veg = input("\nWhat is your first choice of vegtable? (Avacado, Corn, Cucumber, Edamame, Radish, Carrot)\n>").lower()

        if new_order_veg in valid_user_veg:
            poke_bowl_menu_items[-1].append(new_order_veg)
            break
        else:
            print("\n\nInvalid ingredient choice, please try again")
            continue

    while True:
        new_order_veg_two = input("\nWhat is your second choice of vegtable? (Avacado, Corn, Cucumber, Edamame, Radish, Carrot)\n>").lower()

        if new_order_veg_two in valid_user_veg:
            poke_bowl_menu_items[-1].append(new_order_veg)
            break
        else:
            print("\n\nInvalid ingredient choice, please try again")
            continue

    print("Thank you very much for your order!")

"""defines a function that will be the menu interface"""

def menu():
    print("Hello, welcome to Percy's Poke Bowls\n")
    print("1 | Print out the full menu")
    print("2 | Order pre-existing menu items")
    print("3 | Order a custom item")
    print("4 | Exit the program")

    while True:
        try:
            user_menu_choice = int(input("\nType in your choice: \n\n> "))
            if user_menu_choice == 1:
                os.system("clear")
                full_poke_bowl_menu()
                
            elif user_menu_choice == 2:
                os.system("clear")
                order_preexisting_items()
                
            elif user_menu_choice == 3:
                os.system("clear")
                order_custom_item()
            
            elif user_menu_choice == 4:
                return
            
            else:
                continue
            
            while True:
                try:
                    user_menu_choice = input("\n- Do you want to go back to menu (this will stop the program) (yes/no): \n\n>").lower()
                    if user_menu_choice == "yes":
                        menu()
                    elif user_menu_choice == "no":
                        return
                except:
                    user_menu_choice = input("\n- Do you want to go back to menu (this will stop the program) (yes/no): \n\n>").lower()
                    if user_menu_choice == "yes":
                        menu()
                    elif user_menu_choice == "no":
                        return
        except:
            print("\nPlease enter a valid input")
menu()
exit()