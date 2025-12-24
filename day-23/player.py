from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

        self.setheading(90)
        self.up()
        self.shape("turtle")
        self.goto(*STARTING_POSITION)

    def go(self):
        self.forward(MOVE_DISTANCE)

    def retreat(self):
        if self.ycor() > STARTING_POSITION[1]:
            self.backward(MOVE_DISTANCE)

    def check_collision(self, car_list):
        all_cars = car_list
        for car in all_cars:
            if self.distance(car) < 30:
                return (
                    abs(self.xcor() - car.xcor()) < 30
                    and abs(self.ycor() - car.ycor()) < 20
                )
        return False

    def at_finish_line(self, car_man):
        if self.ycor() > FINISH_LINE_Y:
            self.level += 1
            self.goto(*STARTING_POSITION)
            car_man.reset_traffic()
            return True
        return False
