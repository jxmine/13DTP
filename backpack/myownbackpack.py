#write a program to manage a backpack list. 
#The program needs functions that can add, print oand remove items from the backpack
backpack = [("id", "Chocolate", "Yummy" ), ("a", "a", "a")]

def add_item():
    item_id = len(backpack)
    item_name = input("What do you want to add to your backpack?")
    item_desc = input("What is the description of the item?")

    new_item = (item_id, item_name, item_desc)
    backpack.append(new_item)

def print_backpack():
    count = 0
    print(f"{'ID':<20}{'NAME':<20}{'DESCRIPTION':<20}")
    for item in backpack:
        print(f"{count:<20}{item[1]:<20}{item[2]:<20}")
        count += 1

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
            print_backpack()
        elif selection == "2":
            add_item()
        elif selection == "3":
            print_backpack()
            remove_item()
        else:
            print("You did not make a valid selection.")

mainMenu()