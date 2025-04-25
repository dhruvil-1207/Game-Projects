from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        self.make_snake()
        self.head = self.squares[0]
        
    def make_snake(self):
        self.x = 0
        for i in range(3):
            self.add_square((self.x,0))
            self.x-=20

            

    def add_square(self,position):
        s = Turtle("square")
        s.color("white")
        self.squares.append(s)
        s.penup()
        s.goto(position)

    def extend(self):
        self.add_square(self.squares[-1].position())
    
    def move(self):
        for i in range(len(self.squares)-1,0,-1):
            self.squares[i].goto(int(self.squares[i-1].xcor()),int(self.squares[i-1].ycor()))
        self.head.forward(20)
        
        
    
    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
    
    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)


    


