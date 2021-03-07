import random
score = 0
type_of_maths = ()

def get_a_number():
    while True:
        try:
            return int(input("How many questions do you want? "))
            break
        except:
            print("Please type in a number")

num = get_a_number()


while True:
    type_of_maths = input(
"""
What type of maths do you want to do? 
A) Addition 
B) Substraction 
C) Multiplication 
""")
    if type_of_maths.lower() == "a":
        type_of_maths == "a"
        break
    if type_of_maths.lower() == "b":
        type_of_maths == "b"
        break
    if type_of_maths.lower() == "c":
        type_of_maths == "c"
        break
    else:
        print("Please choose either A, B or C")


for i in range(num):
    num_one = int(random.randint(0,10))
    num_two = int(random.randint(0,10))
    
    #addition
    if type_of_maths.lower() == "a":
        question = num_one + num_two
        answer = int(input(f"what is the answer to {num_one} plus {num_two}? "))
        if question == answer:
            score = score + 1
            print(f"Good Job!! \nYour score is now {score}")
        else:
            print(f"You got it wrong :(\nGo learn some more maths \nYour score is now {score}\n")
    
    #substraction
    if type_of_maths.lower() == "b":
        question = num_one - num_two
        answer = int(input(f"what is the answer to {num_one} minus {num_two}? "))
        if question == answer:
            score = score + 1
            print(f"Good Job!! \nYour score is now {score}")
        else:
            print(f"You got it wrong :(\nGo learn some more maths \nYour score is now {score}\n")
    
    #multiplication
    if type_of_maths.lower() == "c":
        question = num_one * num_two
        answer = int(input(f"what is the answer to {num_one} times {num_two}? "))
        if question == answer:
            score = score + 1
            print(f"Good Job!! \nYour score is now {score}")
        else:
            print(f"You got it wrong :(\nGo learn some more maths \nYour score is now {score}\n")
print(f"""
Good job for finishing the quiz!
Your final score is {score} out of {num} questions""")