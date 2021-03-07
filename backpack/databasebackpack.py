#write a program to manage a backpack list. 
#The program needs functions that can add, print oand remove items from the backpack
import sqlite3

DATABASE_FILE = "backpack.db"
backpack = [("1", "Chocolate", "Yummy" ), ("a", "a", "a")]

with sqlite3.connect(DATABASE_FILE) as connection:
    cursor = connection.cursor()
    sql = "SELECT * FROM contents"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)

def print_item():
    count = 0
    print(f"{'ID':<20}{'NAME':<20}{'DESCRIPTION':<20}")
    for item in backpack:
        print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")
        count += 1  


def add_item():
    item_id = len(backpack)
    item_name = input("What do you want to add to your backpack?")
    item_desc = input("What is the description of the item?")

    new_item = (item_id, item_name, item_desc)
    backpack.append(new_item)

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