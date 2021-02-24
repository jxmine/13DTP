#write a program to manage a backpack list. 
#The program needs functions that can add, print oand remove items from the backpack
backpack = [("ID", "NAME", "DESCRIPTION")]

def add_item():
    item_id = len(backpack)
    item_name = input("What do you want to add to your backpack?")
    item_desc = input("What is the description of the item?")

    new_item = (item_id, item_name, item_desc)
    backpack.append(new_item)

def print_item():
    for item in backpack:
        print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")

def remove_item():
    item = int(input("What do you want to remove? \nPlease input the id of the item."))
    backpack.pop(item)

def mainMenu():
    while True:
        print("""
***BACKPACK LIST***
Select a number for the action that you would like to do:
1. View Backpack list
2. Add item to Backpack list
3. Remove item from Backpack list

""")
        selection = input("Make your selection: ")
        if selection == "1":
            print_item()
        elif selection == "2":
            add_item()
        elif selection == "3":
            print_item()
            remove_item()
        else:
            print("You did not make a valid selection.")

mainMenu()