from turtle import *
from random import choice, randint

def spiral(angle, length=10, size=40):
    for line in range(size):
        forward(length + line)
        left(angle)

# Draw lot's of spirals!
def draw_nice_spirals():
    colors = [
        "red",
        "blue",
        "green",
        "yellow"
    ]
    
    speed('fastest')

    for _ in range(200):
        color = choice(colors)
        angle = randint(20, 120)
        length = randint(10, 30)
        size = randint(30, 80)

        print(("Drawing spiral with length " 
               "{}, size {} and angle {} in {}").format(
                   length, size, angle, color))

        pencolor(choice(colors))
        spiral(angle, length, size)
        
# Default spiral
spiral(90)
reset()

# Pattern
draw_nice_spirals()
