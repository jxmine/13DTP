import random
score = 0
a = int(input("How many questions do you want? "))
type_of_maths = input(
"""
What type of maths do you want to do? 
A) Addition 
B) Substraction 
C) Multiplication 
""")

for i in range(a):
    num_one = int(random.randint(0,10))
    num_two = int(random.randint(0,10))
    if type_of_maths.lower() == "a":
        question = num_one + num_two
        answer = int(input(f"what is the answer to {num_one} plus {num_two}? "))
        if question == answer:
            score = score + 1
            print(f"Good Job!! \nYour score is now {score}")
        else:
            print(f"You got it wrong :(\nGo learn some more maths \nYour score is now {score}\n")
    if type_of_maths.lower() == "b":
        question = num_one - num_two
        answer = int(input(f"what is the answer to {num_one} minus {num_two}? "))
        if question == answer:
            score = score + 1
            print(f"Good Job!! \nYour score is now {score}")
        else:
            print(f"You got it wrong :(\nGo learn some more maths \nYour score is now {score}\n")
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
Your final score is {score} out of {a} questions""")