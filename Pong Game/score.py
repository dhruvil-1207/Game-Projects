from turtle import Turtle 
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.red_score = 0
        self.blue_score = 0
        self.penup()
        self.hideturtle()
        self.change_score()
    
    
    def change_score(self):
        self.clear()
        self.color("red")
        self.goto(-175,280)
        self.write(f"Score: {self.red_score}",align = "center",font = ("Courier",12,"bold")) 
        self.color("blue")
        self.goto(125,280)
        self.write(f"Score: {self.blue_score}",align = "center",font = ("Courier",12,"bold"))

    def change_red(self):
        self.red_score+=1
        self.change_score()

    def change_blue(self):
        self.blue_score+=1
        self.change_score()

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER!!",align = "center",font = ("Courier",19,"bold"))
        self.goto(0,-20)
        if(self.red_score == 5 ):
            self.color("white")
            self.write(f"Red Won",align = "center",font = ("Courier",16,"bold"))
        elif(self.blue_score == 5):
            self.color("white")
            self.write(f"Blue Won",align = "center",font = ("Courier",16,"bold"))