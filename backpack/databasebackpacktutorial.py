import sqlite3

DATABASE_FILE = "backpack.db"

#FUNCTIONS
def show_backpack(connection):
    #Nicely print the backpack information
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM contents"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"\n\n{'Name':<20}{'Description':<20}\n")
        for item in results:
            print(f"{item[1]:<20}{item[2]:<60}")
    except:
        print("Something went wrong with connection")

def add_item(connection, item_name, item_description):
    #Add item to backpack database
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO contents(name,description) VALUES (?,?)"
        cursor.execute(sql, (item_name, item_description))
        connection.commit()
    except:
        print("Could not add item")

def delete_item(connection, item_name):
    #Delete an item by name from the database
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM contents WHERE name = ?"
        cursor.execute(sql, (item_name,))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print("Can't find item")
        else:
            connection.commit()
    except:
        print("Item does not exist")

def update_description(connection, item_name, new_description):
    try:
        cursor = connection.cursor()
        sql = "UPDATE contents SET description = ? WHERE name = ?"
        cursor.execute(sql,(new_description, item_name))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print("Can't update item")
        else:
            connection.commit()
    except:
        print("Failed to update item")

with sqlite3.connect(DATABASE_FILE) as connection:
    while True:
        user_input = input("\nWhat do you want to do?\n1: View Backpack Contents\n2: Add Item To Backpack\n3: Delete Item From Backpack\n4: Update Item Description\n5: Exit\n\n")
        if user_input == "1":
            #Print Out Backpack
            show_backpack(connection)
        elif user_input == "2":
            #Get a new item and try to add it
            item_name = input("Item name: \n")
            item_description = input("Description: \n")
            add_item(connection, item_name, item_description)
        elif user_input == "3":
            #Delete an item by name
            item_name = input("Item you would like to delete: \n")
            delete_item(connection, item_name)
        elif user_input == "4":
            #Update an items description
            item_name = input("What item would you like to update?: \n")
            new_description = input("What would you like the new description to be?: \n")
            update_description(connection, item_name, new_description)
        elif user_input == "5":
            print("\n\nGoodbye\n\n")
            break