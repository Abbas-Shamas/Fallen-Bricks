from turtle import Turtle , Screen
import random

Screen = Screen()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.scores = [1,3,5]
        self.highscore = self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.pendown()
        self.first_score()

        # used to call it in the first of the game and when the board is hit by a triangle
    def first_score(self):
        self.clear()
        self.score = 0
        self.write(f"Score {self.score}        Highscore {self.highscore}",align=("center"), font= ("arial",24,"normal"))
        #used to increase the score and write it concequently
    def update_score(self,points):
        self.score += points
        self.clear()
        self.write(f"Score {self.score},        Highscore {self.highscore}",align=("center"), font=("arial",24,"normal"))
        #used to show the game is ended after i turn game_on into False

    def read_highscore(self):
        with open("record.text","r") as file:
            return (int(file.read()))

    def save_highscore(self):
        with open("record.text","w") as file:
            file.write(str(self.highscore))

    def game_over(self):
        self.clear()
        Screen.bgcolor("white")
        self.color("red")
        self.penup()
        self.goto(0,0)
        self.pendown()

        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
    
        self.write(f"-------------Game Over------------ \n\n Final Score: {self.score}\n\n Highscore: {self.highscore}",align=("center"), font=("arial",24,"normal"))

    
        


        


        
