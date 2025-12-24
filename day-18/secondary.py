import random
import turtle as t
from pickletools import dis

colors = ["red", "blue", "cyan", "pink"]
t.colormode(255)
ocean_palette = ["#89CFF0", "#75B84F", "#0066B2", "#FFE5B4"]
screen = t.Screen()


def draw_dashed_line(turtle, length):
    for i in range(round(length)):
        turtle.down()
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)


def draw_sequence(turtle, n):
    for i in range(n):
        turtle.pencolor(random.choice(colors))
        for _ in range(i + 3):
            turtle.forward(100)
            turtle.right(360 / (i + 3))


class Ant(t.Turtle):
    def go_random_path(self, distance):
        angles = [0, 90, 180, 270]
        self.setheading(random.choice(angles))
        self.forward(distance)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b)
    return rgb


ant = Ant()
ant.speed("fastest")


def random_walk(steps, pensize, distance):
    for i in range(steps):
        ant.pencolor(random_color())
        ant.pensize(pensize)
        ant.go_random_path(distance)


def draw_spirograph(n):
    for _ in range(360 // n):
        ant.pencolor(random_color())
        ant.pensize(14)
        ant.circle(100)
        ant.right(1 * n)


draw_spirograph(20)

screen.exitonclick()
