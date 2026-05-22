from turtle import Turtle

class Board(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)
        self.shapesize(1,5)
       

    def right(self):
        self.goto(self.xcor() + 50,self.ycor())

    def left(self):
        self.goto(self.xcor() - 50,self.ycor())