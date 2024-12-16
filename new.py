import steelballrun
import paddlepop
import turtle
import time
import random
import csv


class plinko() :
    def __init__(self):
        self.cash = 1000
        self.peg_list = []
        self.ball_list = []
        self.t = 0
        self.row = 5
        self.cash_perballs = 50
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = self.row * 28
        self.canvas_height = 10 + self.row * 65
        print(self.canvas_width, self.canvas_height)
        self.paddle_list = []
        self.condition = True
        self.screen = turtle.Screen()
        self.screen.listen()
        self.screen.onkey(self.userinp, 'p')
        self.screen.onkey(self.drop, 'l')
        self.screen.onkey(self.changecashperbll1, 'u')
        self.screen.onkey(self.changecashperbll2, 'i')
        self.screen.onkey(self.changecashperbll3, 'o')
        x = -40
        y = 150
        vx = 0
        vy = 0
        rad = 4
        color = (255, 0, 0)
        import copy
        self.jo_list = copy.deepcopy(self.ball_list)
        import copy
        for i in range(3, self.row + 3):
            m = copy.deepcopy(x)
            for j in range(i):
                # print(m,y)
                self.peg_list.append(steelballrun.Ball(rad, m, y, vx, vy, color, i, 'peg', self.row))
                m += 40

            x -= 20
            y -= 100
        y = -self.canvas_height + 10
        for i in range(self.row + 3):
            tom = turtle.Turtle()

            if i == 0 or i == self.row +2 :
                clr = (255,0,0)
                lvl = 0.15
            elif i == round((self.row+3)/2) :
                clr = 'green'
                lvl = 0.2
            elif i %2 == 0 :
                clr = 'yellow'
                lvl = 1.5
            else:
                clr = 'blue'
                lvl = 0.5
            my_paddle = paddlepop.Paddle(35, 10, clr, tom,lvl)
            my_paddle.set_location([x, y])
            x += 40
            self.paddle_list.append(my_paddle)
    def userinp(self):

        q = int(turtle.textinput('cashinput','insert your cash (perballs)'))
        if not isinstance(q,int):
            raise ValueError

        self.cash_perballs = q
    def changecashperbll1(self):
        self.cash_perballs = self.cash/2

    def changecashperbll2(self):
        self.cash_perballs = self.cash / 3

    def changecashperbll3(self):
        self.cash_perballs = self.cash / 4

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        turtle.write(self.cash)
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)
    def __draw_cash(self):
        turtle.penup()
        turtle.goto(-300,200)

        turtle.write(f"your cash {self.cash:.2f}")
        turtle.goto(-300, 150)
        turtle.write(f'cash per ball {self.cash_perballs:.2f}')
    def redraw(self):
        turtle.clear()
        if not self.condition :
            turtle.goto(-200,100)
            turtle.write('Value error')
            turtle.penup()
        for i in self.paddle_list :
            i.clear()
        self.__draw_border()
        self.__draw_cash()
        for i in self.paddle_list:
            i.draw()
        for i in self.peg_list :
            i.draw()
        for i in self.ball_list :
            i.draw()

        turtle.update()
    def drop(self):
        if self.cash_perballs > self.cash :
            self.cash_perballs = self.cash
        elif self.cash ==0 :

            return
        x = random.randint(-10, 10)
        y = 200
        vx = 0
        vy = -15
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.ball_list.append(steelballrun.Ball(6, x, y, vx, vy, ball_color, 0, 'jo', self.row))
        self.cash -= self.cash_perballs
    def __check_collision(self, ball, peg):
        dx = ball.x - peg.x
        dy = ball.y - peg.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= (ball.size + peg.size)
    def checkcondition(self):
        if self.cash <= 0 :
            print('gay')

    def run(self):


        while True :


            while self.condition  :
                self.screen.listen()

                self.redraw()

                for i in self.ball_list:
                    i.move(0.7)
                    for peg in self.peg_list:
                        if self.__check_collision(i, peg):  # Check collision edge-to-edge
                            i.bounce_off(peg)
                    if i.x >= self.canvas_width or i.x <= -self.canvas_width:
                        i.bounce_off_vertical_wall()
                    for pad in self.paddle_list :
                        if i.y <= pad.location[1] + 10 and pad.location[0]-pad.width<i.x< pad.location[0]+pad.width  :
                            self.cash += pad.leverage * self.cash_perballs
                            self.ball_list.remove(i)
                            break

            print('hello world')
            break

                # self.ball_list.remove(i)
if __name__ == '__main__' :
    a = plinko()

    a.run()
    turtle.done()
