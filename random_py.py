import random

a = int(random.randint(0,10))
b = int(random.randint(0,10))

answer = a*b
i = int(input(f"what is the answer to {a} times {b}? "))

if i == answer:
    print("Good job!")

else:
    print("Go and study maths :(")