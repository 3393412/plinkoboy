import turtle
import math


class Ball:
    def __init__(self, size, x, y, vx, vy, color, id,name,row):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100 * size ** 2
        self.count = 0
        self.id = id
        self.row = row
        self.canvas_width = 100
        self.canvas_height = 300
        self.name = name
    def draw(self):
        # draw a circle of radius equals to size centered at (x, y) and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()
        #########################
        # turtle.setheading(0)
        # for i in range(2) :
        #     turtle.forward(self.size)
        #     turtle.left(90)
        #     turtle.forward(self.size)
        #     turtle.left(90)
        # turtle.end_fill()

    def bounce_off_vertical_wall(self):
        self.vx = 0
        self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = 0
        self.count += 1

    def bounce_off(self, that):


        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy;  # dv dot dr
        dist = self.size + that.size  # distance between particle centers at collison

        # magnitude of normal force
        magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)

        # normal force, and in x and y directions
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        # update velocities according to normal force
        if self.name == 'peg':
            that.vx -= fx / 1000

        elif that.name == 'peg' :
            self.vx += fx / 1000
        else :
            self.vx += fx / 10000

            that.vx -= fx / 10000


        # update collision counts
        self.count += 1
        that.count += 1


    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return d

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def __str__(self):
        return str(self.x) + ":" + str(self.y) + ":" + str(self.vx) + ":" + str(self.vy) + ":" + str(self.count) + str(
            self.id)
