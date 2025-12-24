import turtle as t


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.score_1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 150)
        self.write(self.score_2, align="center", font=("Courier", 80, "normal"))

    def increase_score(self, player):
        if player == 1:
            self.score_1 += 1
        else:
            self.score_2 += 1
        self.update_scoreboard()
