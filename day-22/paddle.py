import turtle as t


class Paddle(t.Turtle):
    def __init__(self):
        self.paddle = t.Turtle()
        self.paddle.hideturtle()
        self.paddle.up()
        self.paddle_length = (1, 4)

        self.paddle.setheading(90)
        self.paddle.turtlesize(*self.paddle_length)
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.showturtle()

    def move_up(self):
        upper_bound = 250

        y = self.paddle.ycor()

        if y < upper_bound:
            new_y = y + 20
        else:
            new_y = y

        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        lower_bound = -250
        y = self.paddle.ycor()

        if y > lower_bound:
            new_y = y - 20
        else:
            new_y = y
        self.paddle.goto(self.paddle.xcor(), new_y)
