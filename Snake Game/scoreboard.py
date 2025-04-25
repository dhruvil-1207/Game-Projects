from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0    
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.write(f"Score: {self.score}",align = "center",font = ("Courier",12,"bold")) 

    def change_score(self):
        self.clear()   
        self.score+=1
        self.write(f"Score: {self.score}",align = "center",font = ("Arial",12,"bold"))

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!!",align = "center",font = ("Courier",19,"bold"))
        self.goto(0,-20)
        self.color("white")
        self.write(f"Your Score: {self.score}",align = "center",font = ("Courier",16,"bold"))