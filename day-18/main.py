import random
import turtle as t
from tracemalloc import start

t.colormode(255)
screen = t.Screen()
tom = t.Turtle()
tom.speed(0)

color_list = [
    (246, 244, 243),
    (235, 240, 246),
    (247, 240, 243),
    (240, 246, 243),
    (133, 164, 202),
    (225, 150, 101),
    (30, 43, 64),
    (201, 136, 148),
    (163, 59, 49),
    (236, 212, 88),
    (44, 101, 147),
    (136, 181, 161),
    (148, 64, 72),
    (51, 41, 45),
    (161, 32, 29),
    (60, 115, 99),
    (59, 48, 45),
    (170, 29, 32),
    (215, 83, 73),
    (236, 167, 157),
    (230, 163, 168),
    (36, 61, 55),
    (15, 96, 71),
    (33, 60, 106),
    (172, 188, 219),
    (194, 99, 108),
    (106, 126, 158),
    (18, 83, 105),
    (175, 200, 188),
    (35, 150, 209),
]

start_position = (-(screen.window_width() / 4), -(screen.window_height() / 4))


def init():
    tom.penup()
    tom.goto(start_position)
    tom.pendown()


def draw_dotted_line(turtle, dot_size, spacing, distance):
    for i in range(round(distance)):
        turtle.color(random.choice(color_list))
        turtle.down()
        turtle.dot(dot_size)
        turtle.up()
        turtle.forward(spacing)


width = 10
height = 10
init()

for i in range(1, height + 1):
    draw_dotted_line(tom, 20, 50, width)
    tom.up()
    tom.goto(-(screen.window_width() / 4), start_position[1] + 50 * i)

tom.hideturtle()
screen.exitonclick()
