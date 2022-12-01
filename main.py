import turtle
import random
from math import sqrt


class Figure():
    def __init__(self, window):
        self.window = window
        self.triangle = turtle.Turtle()
        self.point = turtle.Turtle()
        self.X0 = -300
        self.Y0 = -200
        self.a = 600
        self.cur_point = self.Point(X0=self.X0, Y0=self.Y0)
        self.next_point = self.Point(X0=self.X0, Y0=self.Y0)
        self.vertexes = []

        self.point.hideturtle()
        self.point.penup()

        self.draw_triangle()
        self.draw_points()

    def draw_triangle(self):
        self.triangle.hideturtle()
        self.triangle.pensize(3)
        self.triangle.penup()
        self.triangle.goto(self.X0, self.Y0)
        self.triangle.pendown()
        self.triangle.color('black')

        for side in range(3):
            p = self.triangle.pos()
            point = self.Point(x=p[0], y=p[1])
            self.vertexes.append(point)

            self.triangle.fd(self.a)
            self.triangle.left(120)

    def draw_points(self):
        self.cur_point.init_first_point(self.a)
        self.point.goto(self.cur_point.x, self.cur_point.y)
        self.point.dot()
        
        while True:
            vertex = random.randint(0, 2)
            self.cur_point.x = int((max(self.cur_point.x, self.vertexes[vertex].x) -  min(self.cur_point.x, self.vertexes[vertex].x)) / 2)
            self.cur_point.y = int((max(self.cur_point.y, self.vertexes[vertex].y) -  min(self.cur_point.y, self.vertexes[vertex].y)) / 2)

            self.point.goto(self.cur_point.x, self.cur_point.y)
            self.point.dot()

    class Point():
        def __init__(self, x=None, y=None, X0=None, Y0=None):
            self.x = x
            self.y = y
            self.X0 = X0
            self.Y0 = Y0
        
        def init_first_point(self, a):
            self.x = random.randint(0, a)
            max_y = int(self.x * sqrt(3))
            self.x -= abs(self.X0)
            self.y = random.randint(self.Y0, max_y)
            i=0


if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor('white')
    window.setup(800, 800)
    window.title("Треугольник")

    fig = Figure(window)



    # ball = turtle.Turtle('circle')
    # ball.turtlesize(2)
    # ball.hideturtle()
    # ball.color('gold')
    # ball.penup()



    # ball.goto(100, 100)
    # dx, dy = 1.3, 2.3
    # ballX, ballY = 50, 50
    # ball.speed('fastest')

    # while True:
    #     ball.goto(ballX + dx, ballY + dy)
    #     ballX, ballY = ball.xcor(), ball.ycor()
    #     if ballX < -175 or ballX > 175:
    #         dx = dx * -1
            
    #         dy = dy * -1

