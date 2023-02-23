import turtle
import time
from os import kill
from pycparser.c_ast import While

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=0, starty=0)

pen = turtle.Turtle()
pen.speed(0)
kills = []
kill1 = turtle.Turtle()
kill1.shape("circle")
kill1.shapesize(15)
kill1.speed(0)
kill1.up()
kill1.goto(3000, 3000)

kill2 = turtle.Turtle()
kill2.shape("circle")
kill2.shapesize(28)
kill2.speed(0)
kill2.up()
kill2.goto(3000, 3000)

kill3 = turtle.Turtle()
kill3.shape("circle")
kill3.shapesize(15)
kill3.speed(0)
kill3.up()
kill3.goto(3000, 3000)

level = 0


def play_click(mouse_x, mouse_y):
    global level

    q(1000, -370, 150, "black", "black", thickness=10)
    qr(1000, 370, 150, "black", "black", thickness=10)
    kill1.goto(300, 300)
    kill2.goto(-100, -80)
    play.goto(3000, 3000)
    pla.goto(3000, 3000)
    pl.goto(3000, 3000)
    lay.goto(3000, 3000)
    ay.goto(3000, 3000)
    clear()
    level = 1


def play_clic(mouse_x, mouse_y):
    global level

    q(1000, -370, 150, "black", "black", thickness=10)
    qr(1000, 370, 150, "black", "black", thickness=10)
    ht(-170, 0, 150, "black", "black", thickness=10)
    r(100, 0, 150, "black", "black", thickness=10)
    pla.goto(3000, 3000)
    play.goto(3000, 3000)
    pl.goto(3000, 3000)
    lay.goto(3000, 3000)
    ay.goto(3000, 3000)
    clear()
    level = 2


def ply(mouse_x, mouse_y):
    global level

    kol = turtle.Turtle()
    kol.speed(0)
    kol.color("red")
    kol.seth(0)
    kol.up()
    kol.goto(70, -470)
    kol.ht()
    q(1000, -370, 150, "black", "black", thickness=10)
    qr(1000, 370, 150, "black", "black", thickness=10)
    ht(-170, 0, 150, "black", "black", thickness=10)
    r(100, 0, 150, "black", "black", thickness=10)
    kol.write("!Горячие границы!", align="center", font=("Consolas", 50, "normal"))
    kol.goto(70, 470)
    kol.write("!Горячие границы!", align="center", font=("Consolas", 50, "normal"))
    kill1.goto(230, 150)
    kill2.goto(-300, -70)
    kill2.shapesize(15)
    pla.goto(3000, 3000)
    play.goto(3000, 3000)
    pl.goto(3000, 3000)
    lay.goto(3000, 3000)
    ay.goto(3000, 3000)
    clear()
    level = 3


def laf(mouse_x, mouse_y):
    global level

    def kill2_move():
        global kill2_speed
        x = kill2.xcor()
        if kill2.xcor() >= 750 or kill2.xcor() <= 0:
            kill2_speed *= -1
        x += kill2_speed
        kill2.setx(x)

    kill1.goto(300, 300)
    kill2.goto(600, -80)
    kill2.shapesize(15)
    q(1000, -370, 150, "black", "black", thickness=10)
    qr(1000, 370, 150, "black", "black", thickness=10)
    ht(-170, 0, 150, "black", "black", thickness=10)
    r(100, 0, 150, "black", "black", thickness=10)
    pla.goto(3000, 3000)
    play.goto(3000, 3000)
    pl.goto(3000, 3000)
    lay.goto(3000, 3000)
    ay.goto(3000, 3000)
    clear()
    level = 4
    while 1:
        kill2_move()
        is_()


def af(mouse_x, mouse_y):
    global level

    def kill2_move():
        global kill2_speed
        x = kill2.xcor()
        if kill2.xcor() >= 750 or kill2.xcor() <= 0:
            kill2_speed *= -1
        x += kill2_speed
        kill2.setx(x)

    def kill3_move():
        global kill3_speed
        y = kill3.ycor()
        if kill3.ycor() >= 500 or kill3.ycor() <= -500:
            kill3_speed *= -1
        y += kill3_speed
        kill3.sety(y)

    kill1.goto(300, 300)
    kill2.goto(600, -80)
    kill3.goto(0, 0)
    kill2.shapesize(15)
    q(1000, -370, 150, "black", "black", thickness=10)
    qr(1000, 370, 150, "black", "black", thickness=10)
    ht(-170, 0, 150, "black", "black", thickness=10)
    r(100, 0, 150, "black", "black", thickness=10)
    pla.goto(3000, 3000)
    play.goto(3000, 3000)
    pl.goto(3000, 3000)
    lay.goto(3000, 3000)
    ay.goto(3000, 3000)
    clear()
    level = 5
    while 1:
        kill2_move()
        kill3_move()
        s_()


def q(x, y, length, line_color="red", fill_color="green", thickness=1):
    pen.shape("turtle")
    pen.seth(90)
    pen.color(line_color, fill_color)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fd(90)
    pen.lt(90)
    pen.fd(90000)
    pen.lt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(90000)
    pen.end_fill()


def qr(x, y, length, line_color="red", fill_color="green", thickness=1):
    pen.shape("turtle")
    pen.seth(90)
    pen.color(line_color, fill_color)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fd(90)
    pen.lt(90)
    pen.fd(90000)
    pen.lt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(90000)
    pen.end_fill()


def ht(x, y, length, line_color="red", fill_color="green", thickness=1):
    pen.shape("turtle")
    pen.seth(0)
    pen.color(line_color, fill_color)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fd(90)
    pen.lt(90)
    pen.fd(400)
    pen.lt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(90)
    pen.end_fill()


def r(x, y, length, line_color="red", fill_color="green", thickness=1):
    pen.shape("turtle")
    pen.seth(90)
    pen.color(line_color, fill_color)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fd(90)
    pen.lt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(400)
    pen.lt(90)
    pen.fd(90)
    pen.end_fill()


def clear():
    p.undo()
    g.undo()
    pf.undo()
    gr.undo()
    rl.undo()


play = turtle.Turtle()
play.speed(0)
play.shape("square")
play.color("black")
play.shapesize(15, 20)
play.seth(0)
play.up()
play.goto(-730, 70)

lay = turtle.Turtle()
lay.speed(0)
lay.shape("square")
lay.color("black")
lay.shapesize(10, 15)
lay.seth(0)
lay.up()
lay.goto(-350, -300)


ay = turtle.Turtle()
ay.speed(0)
ay.shape("square")
ay.color("black")
ay.shapesize(10, 15)
ay.seth(0)
ay.up()
ay.goto(400, -300)


pla = turtle.Turtle()
pla.speed(0)
pla.shape("square")
pla.color("black")
pla.shapesize(15, 20)
pla.seth(0)
pla.up()
pla.goto(73, 70)

pl = turtle.Turtle()
pl.speed(0)
pl.shape("square")
pl.color("black")
pl.shapesize(15, 20)
pl.seth(0)
pl.up()
pl.goto(730, 70)


p = turtle.Turtle()
p.speed(0)
p.color("red")
p.seth(0)
p.up()
p.goto(-770, -200)
p.ht()
p.write(" 1 level", align="center", font=("Consolas", 30, "normal"))

pf = turtle.Turtle()
pf.speed(0)
pf.color("red")
pf.seth(0)
pf.up()
pf.goto(100, -200)
pf.ht()
pf.write(" 2 level", align="center", font=("Consolas", 30, "normal"))

g = turtle.Turtle()
g.speed(0)
g.color("red")
g.seth(0)
g.up()
g.goto(770, -200)
g.ht()
g.write(" 3 level", align="center", font=("Consolas", 30, "normal"))

gr = turtle.Turtle()
gr.speed(0)
gr.color("red")
gr.seth(0)
gr.up()
gr.goto(-370, -450)
gr.ht()
gr.write(" 4 level", align="center", font=("Consolas", 30, "normal"))


rl = turtle.Turtle()
rl.speed(0)
rl.color("red")
rl.seth(0)
rl.up()
rl.goto(370, -460)
rl.ht()
rl.write(" 5 level", align="center", font=("Consolas", 30, "normal"))


player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("green")
player.shapesize(2, 2, 2)
player.seth(0)
player.up()
player.goto(-810, 70)


def move_right():
    if hp:
        x = player.xcor()
        if player.xcor() < 960:
            x += 10
            player.setx(x)
            is_touch()
            touch()
            touc()
            is_()
            if player.xcor() > 900 and level == 1:
                play_clic(0, 0)
                kill1.goto(3000, 3000)
                kill2.goto(3000, 3000)
                player.goto(-810, 70)
            if player.xcor() > 900 and level == 2:
                ply(0, 0)
                player.goto(-810, 70)
            if player.xcor() > 900 and level == 3:
                player.goto(-810, 70)
                clear()
                laf(0, 0)
            if player.xcor() > 900 and level == 4:
                player.goto(-810, 70)
                clear()
                af(0, 0)


def move_left():
    if hp:
        x = player.xcor()
        if player.xcor() > -960:
            x -= 10
            player.setx(x)
            is_touch()
            touch()
            touc()
            is_()


def move_up():
    if hp:
        y = player.ycor()
        if player.ycor() < 370:
            y += 10
            player.sety(y)
            is_touch()
            touch()
            touc()
            is_()


def move_down():
    if hp:
        y = player.ycor()
        if player.ycor() > -255:
            y -= 10
            player.sety(y)
            is_touch()
            touch()
            touc()
            is_()


def is_touch():
    global hp
    if level == 1:
        if player.distance(kill1) <= 170 or player.distance(kill2) <= 300:
            player.ht()
            hp = False


def touch():
    global hp
    if level == 2:
        if player.xcor() > -200 and player.xcor() < -60 and player.ycor() > -20 and player.ycor() < 500:
            player.ht()
            hp = False

        if player.xcor() > -10 and player.xcor() < 110 and player.ycor() > -500 and player.ycor() < 110:
            player.ht()
            hp = False


def touc():
    global hp
    if level == 3:
        if player.ycor() < -255 or player.ycor() > 340:
            player.ht()
            hp = False

        if player.xcor() > -200 and player.xcor() < -60 and player.ycor() > -20 and player.ycor() < 500:
            player.ht()
            hp = False

        if player.xcor() > -10 and player.xcor() < 110 and player.ycor() > -500 and player.ycor() < 110:
            player.ht()
            hp = False
        if player.distance(kill1) <= 170 or player.distance(kill2) <= 170:
            player.ht()
            hp = False


def is_():
    global hp
    if level == 4:
        if player.distance(kill1) <= 170 or player.distance(kill2) <= 170:
            player.ht()
            hp = False
        if player.ycor() < -255 or player.ycor() > 340:
            player.ht()
            hp = False
        if player.xcor() > -200 and player.xcor() < -60 and player.ycor() > -20 and player.ycor() < 500:
            player.ht()
            hp = False

        if player.xcor() > -10 and player.xcor() < 110 and player.ycor() > -500 and player.ycor() < 110:
            player.ht()
            hp = False


def s_():
    global hp
    if level == 5:
        if player.distance(kill1) <= 170 or player.distance(kill2) <= 170 or player.distance(kill3) <= 170:
            player.ht()
            hp = False
        if player.ycor() < -255 or player.ycor() > 340:
            player.ht()
            hp = False
        if player.xcor() > -200 and player.xcor() < -60 and player.ycor() > -20 and player.ycor() < 500:
            player.ht()
            hp = False

        if player.xcor() > -10 and player.xcor() < 110 and player.ycor() > -500 and player.ycor() < 110:
            player.ht()
            hp = False


kill2_speed = 5
kill3_speed = 5
hp = True

screen = turtle.Screen()
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_up, "Up")
screen.listen()
play.onclick(play_click)
pla.onclick(play_clic)
pl.onclick(ply)
lay.onclick(laf)
ay.onclick(af)


screen.mainloop()