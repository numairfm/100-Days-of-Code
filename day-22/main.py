import time
import turtle as t

from ball import Ball
from environment import Environment
from paddle import Paddle

env = Environment()
print(env.screen.canvwidth, env.screen.canvheight)
ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()

paddle1.paddle.goto(-env.screen.canvwidth, 0)
paddle2.paddle.goto(env.screen.canvwidth, 0)

env.input_handler(paddle1, paddle2)

running = True
while running:
    ball.bounce()
    env.handle_collisions(paddle1, paddle2, ball)

    env.screen.update()
    time.sleep(0.01)
