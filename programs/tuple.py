backpack = []

def print_backpack():
    for item in backpack:
        print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")

title = ("ID", "NAME", "DESCRIPTION")
item1 = (14, "hello", "yay")
item2 = ("sdkj", 6, "dkjshf")

item_one = input("What items do you want to add to your backpack?")
item_two = input("What items do you want to add to your backpack?")
item_three = input("What items do you want to add to your backpack?")

item3 = (item_one, item_two, item_three)

backpack.append(title)
backpack.append(item1)
backpack.append(item2)
backpack.append(item3)

print_backpack()
