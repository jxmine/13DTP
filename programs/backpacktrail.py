backpack = ["food", "water", "map","torch"]

def add(item):
    return input("What do you want to add?")

#add dress
backpack.append("dress")
print(backpack)

backpack.remove("water")
print(backpack)

for item in backpack:
    print(item)

#write a program to manage a backpack list. 
#The program needs functions that can add, print oand remove items from the backpack