import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 0.5


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.looped_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_traffic(self):
        for i in range(25):
            random_color = random.choice(COLORS)
            new_car = Turtle()
            new_car.hideturtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.up()
            new_car.color(random_color)
            new_car.goto(random.randrange(0, 800, 10), random.randrange(-220, 250, 1))
            self.all_cars.append(new_car)

    def loop_traffic(self):
        for car in self.looped_cars:
            self.looped_cars.pop(0)
            car.goto(330, random.randrange(-220, 250, 10))

    def drive_cars(self):
        for car in self.all_cars:
            if car.xcor() < 330:
                car.showturtle()
            car.forward(self.car_speed)
            if car.xcor() < -330:
                self.looped_cars.append(car)
                self.loop_traffic()

    def update_speed(self, level):
        if level < 3:
            self.car_speed = 0.5
        elif level < 3:
            self.car_speed = 1
        elif level < 9:
            self.car_speed = 1.5
        elif level < 12:
            self.car_speed = 2

    def reset_traffic(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars = []
        self.looped_cars = []
        self.__init__()
        self.create_traffic()
        return True
