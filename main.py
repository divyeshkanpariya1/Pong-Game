from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(width=1200, height=700)
scr.bgcolor('black')
scr.title("My Pong Game")
scr.tracer(0)

paddle_1 = Paddle(-570)
paddle_2 = Paddle(+570)

score = Scoreboard()
score.show_score()
ball = Ball()

scr.listen()

scr.onkeypress(paddle_1.up, "w")
scr.onkeypress(paddle_1.down, "s")
scr.onkeypress(paddle_2.up, "Up")
scr.onkeypress(paddle_2.down, "Down")

game_finish = False

while not game_finish:

    if score.r_score == 10 or score.l_score == 10:
        game_finish = True
    else:
        time.sleep(ball.move_speed)
        scr.update()
        ball.move_ball()

        if paddle_1.distance(ball) < 40 and ball.xcor() <= -560:
            ball.change_dir()

        elif paddle_2.distance(ball) < 40 and ball.xcor() >= 560:
            ball.change_dir()

        if ball.xcor() > 580:
            ball.starting_pos()
            score.l_update()

        elif ball.xcor() < -580:
            ball.starting_pos()
            score.r_update()

score.result()

scr.exitonclick()
