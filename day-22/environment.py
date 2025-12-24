import turtle as t

import score_board


class Environment(score_board.ScoreBoard):
    def __init__(self):
        super().__init__()
        self.score_board = score_board.ScoreBoard()

        self.screen = t.Screen()
        self.screen.setup(width=1000, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.listen()
        self.screen.tracer(0)

        self.score_board.update_scoreboard()

    def input_handler(self, paddle1, paddle2):
        self.screen.onkeypress(key="w", fun=paddle1.move_up)
        self.screen.onkeypress(key="s", fun=paddle1.move_down)

        self.screen.onkeypress(key="Up", fun=paddle2.move_up)
        self.screen.onkeypress(key="Down", fun=paddle2.move_down)

    def score(self, half):
        if half < 0:
            self.score_board.increase_score(1)
        else:
            self.score_board.increase_score(2)

    def handle_collisions(self, paddle1, paddle2, ball):
        paddle1_top = paddle1.paddle.ycor() + 40
        paddle1_bottom = paddle1.paddle.ycor() - 40

        paddle2_top = paddle2.paddle.ycor() + 40
        paddle2_bottom = paddle2.paddle.ycor() - 40

        if ball.ball.ycor() < ball.lower_bound or ball.ball.ycor() > ball.upper_bound:
            ball.swap_y()

        if ball.ball.xcor() < ball.left_bound or ball.ball.xcor() > ball.right_bound:
            ball.swap_x()
            self.score(ball.ball.xcor())
            ball.ball.goto(ball.start_position)

            print(self.score_board.score_1, self.score_board.score_2)

        if paddle1_bottom < ball.ball.ycor() < paddle1_top:
            if abs(ball.ball.xcor() - paddle1.paddle.xcor()) < 20:
                ball.swap_x()

        if paddle2_bottom < ball.ball.ycor() < paddle2_top:
            if abs(ball.ball.xcor() - paddle2.paddle.xcor()) < 20:
                ball.swap_x()
