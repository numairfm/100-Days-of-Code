import turtle


class Etcher(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.screen = turtle.Screen()
        self.screen.listen()
        self.shape("turtle")
        self.color("black")
        self.speed("fastest")

    def move_forwards(self):
        self.forward(10)

    def move_backwards(self):
        self.backward(10)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def control(self):
        self.screen.onkey(key="w", fun=self.move_forwards)
        self.screen.onkey(key="s", fun=self.move_backwards)
        self.screen.onkey(key="a", fun=self.turn_left)
        self.screen.onkey(key="d", fun=self.turn_right)
        self.screen.onkey(key="c", fun=self.clear_screen)

    def clear_screen(self):
        self.clear()
        self.penup()
        self.home()
        self.pendown()


tim = Etcher()

tim.control()

tim.screen.exitonclick()
