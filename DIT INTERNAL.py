"""this program allows users to choose and order poke bowls"""

import os
import time

# list of menu items 
poke_bowl_menu_items = [["1:", "Salmon", "Rice", "Avacado", "Corn", 22],["2:", "Tuna", "Rice", "Avacado", "Radish", 22],["3:", "Tofu", "Rice", "Radish", "Cucumber", 27],["4:", "Snapper", "Rice", "Corn", "Edamame", 25],["5:", "Teriyaki Chicken", "Rice", "Seaweed", "Carrot", 22]]

# stores the users orders in this list
poke_bowl_orders = [[]]

# defines a function that prints out the full menu
def full_poke_bowl_menu():
    for poke_bowl_menu_item in poke_bowl_menu_items:
        print("------------------------------------")
        print(poke_bowl_menu_item[0], poke_bowl_menu_item[1], poke_bowl_menu_item[2], poke_bowl_menu_item[3], poke_bowl_menu_item[4], poke_bowl_menu_item[5])

     

# defines a function that allows users to order pre-exisitng items 
def order_preexisting_items():
    os.system("clear")
    
    for poke_bowl_menu_item in poke_bowl_menu_items:
        print("------------------------------------")
        print(poke_bowl_menu_item[0], poke_bowl_menu_item[1], poke_bowl_menu_item[2], poke_bowl_menu_item[3], poke_bowl_menu_item[4], poke_bowl_menu_item[5])

    user_order = input("\n\n\nWhat would you like to order?\n\n>")

    while True:
        try:  
            if user_order == 1:
                print(poke_bowl_menu_item[0])
            elif user_order == 2:
                print(poke_bowl_menu_item[0])
            elif user_order == 3:
                print(poke_bowl_menu_item[0])
            elif user_order == 4:
                print(poke_bowl_menu_item[0])
            elif user_order == 5:
                print(poke_bowl_menu_item[0])
            
            
        except ValueError:
            print("please enter a valid choice")
            
                            
            
        while True:
            try:
                user_menu_choice = input("\n- Do you want to order something else? (yes/no): \n\n>").lower()
                if user_menu_choice == "yes":
                    order_preexisting_items()
                elif user_menu_choice == "no":
                    "Thank you for placing your order!"
            except:
                print("invalid input")
                            

def order_custom_item():
    poke_bowl_menu_items.append([])
    new_order_protein = input("what is your Protein? (Salmon, Tuna, Snapper, Chicken, Tofu)\n\n>")
    poke_bowl_menu_items[-1].append(new_order_protein)
    os.system("clear")
    new_order_carbs = input("What is your base? (Rice, Brown Rice)\n\n>")
    poke_bowl_menu_items[-1].append(new_order_carbs)
    os.system("clear")
    new_order_veg = int(input("What do you want as your first topping? (1. Avacado, 2. Corn, 3. Cucumber, 4. Edamame, 5. Radish, 6. Carrot)\n\n>"))
    poke_bowl_menu_items[-1].append(new_order_veg)
    os.system("clear")
    new_order_veg_two = input("What do you want as your second topping? (Avacado, Corn, Cucumber, Edamame, Radish, Carrot)\n\n>")
    poke_bowl_menu_items[-1].append(new_order_veg_two)
    os.system("clear")
    price = 28
    print(f"Your price is 28$")
    poke_bowl_menu_items[-1].append(price)
    print(poke_bowl_menu_items[-1])
    
    
# defines a function that will be the menu interface

def menu():
    print("Hello, welcome to Percy's Poke Bowls\n")
    print("1 | Print out the full menu")
    print("3 | Order Pre-existing menu items")
    print("4 | Order a Custom Item")
    print("5 | Exit the program")

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
                exit()
            
            else:
                continue
            
            while True:
                try:
                    user_menu_choice = input("\n- Do you want to go back to menu (yes/no): \n\n>").lower()
                    if user_menu_choice == "yes":
                        menu()
                    elif user_menu_choice == "no":
                        return
                except:
                    print("invalid input")
                    
            
        except:
            print("\nPlease enter a valid input")
            
    


    
menu()