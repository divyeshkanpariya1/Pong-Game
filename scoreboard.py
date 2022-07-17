from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

    def show_score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-70, 300)
        self.write(f"{self.l_score}", True, "center", ("Arial", 30, "bold"))
        self.goto(70, 300)
        self.write(f"{self.r_score}", True, "center", ("Arial", 30, "bold"))

    def l_update(self):
        self.l_score += 1
        self.clear()
        self.show_score()

    def r_update(self):
        self.r_score += 1
        self.clear()
        self.show_score()

    def result(self):
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write(f"Game Finished!!\nPlayer 1 is winner.", True, "center", ("Arial", 40, "bold"))
        else:
            self.write(f"Game Finished!!\nPlayer 2 is winner.", True, "center", ("Arial", 40, "bold"))
