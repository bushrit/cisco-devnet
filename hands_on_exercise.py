"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("pi value is", pi,"and the type is", type(pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("i is less than 50")
elif i == 50:
    print("i is equal to 50")
else:
    print("i is greater than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print(picked_fruit , "is orange")
elif picked_fruit == 'strawberry':
    print(picked_fruit , "is red")
elif picked_fruit == 'banana':
    print(picked_fruit , "is yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def x2n(a, b):
    c = a*b
    return c

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", x2n(12,96))

print("48 x 17 =", x2n(48,17))

print("196523 x 87323 =", x2n(196523,87323))
