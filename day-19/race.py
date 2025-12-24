import random
import turtle as t

color_list = ["red", "blue", "pink", "yellow", "purple", "cyan"]


class Racer(t.Turtle):
    def __init__(self, y_pos):
        super().__init__(shape="turtle")
        self.penup()
        self.goto(-450, y_pos)

    def gogogo(self):
        if random.randint(1, 20) == 20:
            self.forward(10)


class Race:
    def __init__(self):
        self.all_racers = []

    def setup_screen(self):
        self.screen = t.Screen()
        self.screen.exitonclick()

    def define_contestants(self, number):
        for i in range(number):
            color_index = i % len(color_list)
            new_contestant = Racer((i * 50) - (number * 20))
            new_contestant.color(color_list[color_index])
            self.all_racers.append(new_contestant)

    def start_race(self):
        race_on = True
        while race_on:
            for obj in self.all_racers:
                obj.gogogo()
                if obj.position()[0] > 450:
                    print(f"{str(obj.pencolor()).title()} Turtle Wins")
                    return obj


race = Race()
race.define_contestants(10)
race.start_race()

race.setup_screen()
