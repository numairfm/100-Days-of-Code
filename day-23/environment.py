import turtle as t

from player import Player


class Environment(t.Turtle):
    def __init__(self):
        self.screen = t.Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.listen()

    def update(self):
        self.screen.update()

    def handle_input(self, obj):
        self.screen.onkey(obj.go, "w")
        self.screen.onkey(obj.retreat, "s")
