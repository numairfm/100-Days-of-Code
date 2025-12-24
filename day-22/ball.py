import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        self.lower_bound = -290
        self.upper_bound = self.lower_bound * -1
        self.left_bound = -490
        self.right_bound = self.left_bound * -1

        self.x_speed = 2
        self.y_speed = 2

        self.ball = t.Turtle()
        self.ball.up()
        self.start_position = (self.ball.xcor(), self.ball.ycor())

        self.ball.color("white")
        self.ball.shape("circle")

    def bounce(self):
        new_x = self.ball.xcor() + self.x_speed
        new_y = self.ball.ycor() + self.y_speed
        self.ball.goto(new_x, new_y)

    def swap_y(self):
        if self.y_speed > 0:
            self.y_speed += 0.01
        else:
            self.y_speed -= 0.01
        self.y_speed *= -1

    def swap_x(self):
        self.x_speed *= -1
