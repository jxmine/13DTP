backpack_title = [("ID", "NAME", "DESCRIPTION")]
backpack = [("id", "Chocolate", "Yummy" ), ("a", "a", "a")]

def add_item():
    item_id = len(backpack)
    item_name = input("What do you want to add to your backpack? ")
    item_desc = input("What is the description of the item? ")
    new_item = (item_id, item_name, item_desc)
    backpack.append(new_item)

def print_backpack():
    count = 0
    for item in backpack_title:
        print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")
    for item in backpack:
        print(f"{count:<20}{item[1]:<20}{item[2]:<20}")
        count += 1

def remove_item():
    item = int(input("What do you want to remove? \nPlease input the id of the item. "))
    backpack.pop(item)

def check_item():
    wanted_item = input("Enter an item that you would like to check if it's in the backpack. ")
    found_item = [item for item in backpack if item[1] == wanted_item]
    print(found_item)

    if backpack[1] in backpack == wanted_item:
        print("It's in the backpack!")
    else:
        not_in_backpack = input("It's not in the backpack. Would you like to add it in the backpack? ")
        if not_in_backpack.lower() == "yes":
            item_desc = input("What is the description of the item? ")
            new_item = (1, wanted_item, item_desc)
            backpack.append(new_item)

def mainMenu():
    while True:
        print("""
***BACKPACK LIST***
Select a number for the action that you would like to do:
1. View backpack 
2. Add item to backpack 
3. Remove item from backpack 
4. Check if item is in the backpack 

""")
        selection = input("Make your selection: ")
        if selection == "1":
            print_backpack()
        elif selection == "2":
            print_backpack()
            add_item()
        elif selection == "3":
            print_backpack()
            remove_item()
        elif selection == "4":
            check_item()
            print_backpack()
        else:
            print("You did not make a valid selection.")

mainMenu()