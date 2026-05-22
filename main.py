from turtle import Screen
from board import Board
from bricks import Brick
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Fallen bricks")
screen.tracer(0)

board = Board((0,-250))
brick = Brick()
score = Score()



screen.listen()
screen.onkey(board.right,"Right")
screen.onkey(board.left,"Left")

game_on = True
while game_on:
    brick.falling()
    # moving the brick(we can remove the while loop totally but we should put the screen update on the top of the loop!!!)
    while brick.ycor() != -300:
        brick.goto(brick.xcor(),brick.ycor() + brick.y_move)
        screen.update()
        time.sleep(0.05)
        #checking the distance and adding the score
        if brick.ycor() >= -230 and brick.distance(board) <= 50:
            #reset the score
            if brick.shape() == "triangle":
                score.first_score()
            #game_over
            elif brick.shape() == "turtle": 
                if brick.color()[0] == "white":
                    score.game_over()
                    game_on = False
                    screen.update()

                else:# increase the score normally
                    score.update_score(5)
            #if nothing happened the score will increase succefully

            elif brick.shape() == "square":
                score.update_score(2)
            
            elif brick.shape() == "circle":
                score.update_score(1)
            #return to the beginning
            break














screen.exitonclick()