import random
import time
import turtle as t

color_list = ["chartreuse3", "chartreuse2", "chartreuse1"]


class Snake(t.Turtle):
    def __init__(self):
        self.segments = []
        self.head = t.Turtle("square")
        self.head.color("chartreuse4")
        self.head.penup()
        self.direction = "right"
        self.can_turn = True
        self.is_dead = False
        self.score = 0

    def collision_check(self):
        x = self.head.xcor()
        y = self.head.ycor()

        if x > 290 or x < -290 or y > 290 or y < -290:
            self.is_dead = True

        for segment in self.segments[2:]:
            if segment.distance(self.head.position()) < 10:
                self.is_dead = True

    def fruit_check(self, fruit_obj):
        if self.head.distance(fruit_obj.fruit) < 15:
            self.score += 1
            fruit_obj.spawn()
            self.extend()

        for segment in self.segments:
            if segment.distance(fruit_obj.fruit) < 15:
                fruit_obj.spawn()

    def update_seg_colors(self):
        if len(self.segments) == 0:
            return

        for i in range(len(self.segments)):
            if i < len(self.segments) * 0.1:
                self.segments[i].color(color_list[0])
            elif i < len(self.segments) * 0.4:
                self.segments[i].color(color_list[1])
            else:
                self.segments[i].color(color_list[2])

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.update_seg_colors()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        if len(self.segments) > 0:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())

        if self.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.direction == "right":
            self.head.setx(self.head.xcor() + 20)

        self.can_turn = True

    def go_up(self):
        if self.direction != "down" and self.can_turn:
            self.direction = "up"
            self.can_turn = False

    def go_down(self):
        if self.direction != "up" and self.can_turn:
            self.direction = "down"
            self.can_turn = False

    def go_left(self):
        if self.direction != "right" and self.can_turn:
            self.direction = "left"
            self.can_turn = False

    def go_right(self):
        if self.direction != "left" and self.can_turn:
            self.direction = "right"
            self.can_turn = False


class Fruit(t.Turtle):
    def __init__(self):
        self.fruit = t.Turtle("circle")
        self.fruit.color("red")
        self.fruit.penup()

    def spawn(self):
        self.grid_x = random.randrange(-280, 280, 20)
        self.grid_y = random.randrange(-280, 280, 20)

        self.fruit.goto(self.grid_x, self.grid_y)


class GameEnvironment(t.Turtle):
    def __init__(self):
        self.screen = t.Screen()
        self.screen.setup(600, 600)
        self.screen.tracer(0)
        self.screen.listen()

        w = self.screen.window_width()
        h = self.screen.window_height()

        self.border = t.Turtle()
        self.border.speed(0)
        self.border.hideturtle()
        self.border.penup()

        left_edge = -w / 2
        top_edge = h / 2

        self.border.goto(left_edge, top_edge)
        self.border.pendown()
        self.border.pensize(5)
        self.border.color("red")

        for _ in range(2):
            self.border.forward(w)
            self.border.right(90)
            self.border.forward(h)
            self.border.right(90)

    def update_title(self):
        self.screen.title(f"{snake.score}")

    def allow_exit_on_click(self):
        self.screen.exitonclick()

    def listen_for_input(self, snake):
        self.screen.onkeypress(snake.go_up, "w")
        self.screen.onkeypress(snake.go_down, "s")
        self.screen.onkeypress(snake.go_left, "a")
        self.screen.onkeypress(snake.go_right, "d")


snake = Snake()
game = GameEnvironment()
game.listen_for_input(snake)

snake.add_segment((0, 0))
snake.extend()
snake.update_seg_colors()

fruit = Fruit()
fruit.spawn()

running = True
while running:
    snake.collision_check()
    snake.fruit_check(fruit)
    snake.move()

    if snake.is_dead:
        break

    game.update_title()
    game.screen.update()
    time.sleep(0.125)


print("dead asl")
game.allow_exit_on_click()
