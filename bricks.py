from turtle import Turtle 
import random

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shapes = ["circle","triangle","turtle","square","turtle"]
        self.colors = ["red","white","green","blue","white"]
        self.penup()
        self.y_move = -10
        
        #moving the brick from the top to the bottom of the screen
    def falling(self):
        self.shape(random.choice(self.shapes))
        self.color(random.choice(self.colors))
        self.shapesize(random.uniform(0.5 , 2))
        self.goto(random.randint(-350,350) , 300)
       


