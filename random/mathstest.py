import random

def addition(num_one, num_two):
    return int(num_one + num_two)

name = input("Hello, what is your name?")

for i in range(10):
    num_one = random.randint(0,100)
    num_two = random.randint(0,100)
    type_of_maths = input(f"""
Hello, {name} what type of maths do you want to do today?
A) Addition
B) Substraction
C) Multiplication
""")
    if type_of_maths.lower == "a":
        question = int(input(f"what is the answer to {num_one} plus {num_two}"))
        answer = addition(num_one, num_two)
        if answer == question:
            print("Good Job!")
