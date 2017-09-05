from turtle import *

def squares(n):
    for i in range(n):
        square(20)
        penup()
        forward(30)
        left(24)
        pendown()

def pattern():
    reset()
    speed(10)                   # max speed
    pencolor('green')
    # 15 squares because there is a turn 24 degrees between each,
    # and 15*24 = 360, a full circle
    squares(15)
    forward(25)
    left(80)
    pencolor('red')
    fillcolor('yellow')
    for x in range(100, 130):
        forward(x)
        begin_fill()
        circle(10)
        end_fill()
        left(80)
        
