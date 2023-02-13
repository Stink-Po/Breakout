from turtle import Screen
from paddle import Paddle
from breacks import MakeBobbles
from ball import Ball
from score import Score
import time
from constence import *

# boolean vars
start = False
touch_left = False
touch_right = False
touch_up = False
game_is_on = True

# init screen
screen = Screen()
screen.bgcolor(colors[4])
screen.setup(width, height)
screen.tracer(0)
# init classes

paddle = Paddle()
s = MakeBobbles()
s.build_row()
ball = Ball()
screen.listen()
score = Score()
# init database


screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")


def getting_high_score(new_record):
    if score_data:
        high_score = new_record
        if score_data.record < high_score:
            edit_row = session.query(data).filter_by(id=1).first()
            edit_row.record = high_score
            edit_row.time = today
            session.commit()
            return high_score
        else:
            return score_data.record
    else:
        add_row = database.ScoresData(time=today, record=0)
        session.add(add_row)
        session.commit()
        return 0


def game():
    global touch_up, touch_right, touch_left, game_is_on
    while game_is_on:
        current_score = score.score
        score.write_score()
        if score.lives == 0:
            getting_high_score(current_score)

            screen.clear()
            screen.bgcolor(colors[4])
            score.write_final()
            game_is_on = False
        time.sleep(ball.speed)
        ball.start_move()
        screen.update()
        if ball.xcor() < -480 or ball.xcor() > 480:
            if ball.xcor() < -480:
                touch_left = True
            if ball.xcor() > 480:
                touch_right = True
            ball.bounce_wall()
        if ball.ycor() > 280:
            touch_up = True
            ball.bounce_top()
        if ball.ycor() < -270:
            ball.reset_ball()
            score.lives -= 1
        if ball.distance(paddle) < 40:
            ball.bounce_paddle()
        if len(s.bobble_list) != 0:
            for item in s.bobble_list:
                if ball.distance(item) < 30:
                    score.add_score(color=item.color()[0])
                    s.bobble_list.remove(item)
                    item.undo()
                    ball.bounce_bobble(touch_left,
                                       touch_right,
                                       touch_up)
                    ball.speed *= 0.9
                touch_up, touch_left, touch_right = False, False, False
        else:
            getting_high_score(current_score)
            game_is_on = False


game()
screen.mainloop()
