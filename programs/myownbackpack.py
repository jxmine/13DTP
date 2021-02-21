def mainmenu():
    while True:
        try:
            choice = int(input("""
What do you want to do today?
1. View backpack list
2. Add an item to the backpack
3. Delete an item from the backpack
4. Check the amount of items in the backpack 
5. Clear the backpack
"""))
            break
        except:
            print("choose a valid option!")
        print("hello")

mainmenu()

def view():
    backpack.list
    