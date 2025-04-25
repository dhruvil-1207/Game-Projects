from turtle import Turtle

UP = 90
DOWN = 270

class Racket(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.goto(position)
    
    def mid_line(self):
        self.color("grey")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=30,stretch_wid=0.5)
        self.shape("circle")


    def racket_up(self):
        if(self.ycor()<250):
            self.goto(self.xcor(),self.ycor()+30)

    def racket_down(self):
        if(self.ycor()>-250):
            self.goto(self.xcor(),self.ycor()-30)

