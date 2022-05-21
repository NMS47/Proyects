from turtle import Turtle

class States(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    def place_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, True, 'center', ('Arial', 12, 'bold'))

