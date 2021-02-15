def addition(num_one, num_two):
    return int(num_one + num_two)
    
while True:
    try:
        first_num = int(input("Choose a number "))
        second_num = int(input("Choose another number to add to the previous number "))
        total = addition(first_num, second_num)
        break
    except:
        print("Please choose a number")

 
print(f" The total is {total}")

