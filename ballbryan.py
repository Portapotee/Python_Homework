from turtle import *
from freegames import vector
from random import *

t1 = Turtle(visible=False)
t1.pu()
screen = Screen()
bg_img = r'field.png'
screen.bgpic(bg_img)
bird_img = 'bird.gif'
bird_dead = 'falling_bird_img_9.gif'
screen.addshape(bird_img)
screen.addshape(bird_dead)

bird = Turtle()
bird.shape(bird_img)
bird.pu()
birdstartx = 350
birdstarty = 200
birdpos = vector(birdstartx,birdstarty)
bird.hideturtle()
bird.goto(birdpos.x,birdpos.y)
bird.showturtle()
birdspeed = vector(0,0)
birdhitted = False

def draw():
    global birdhitted
    t1.pu
    t1.clear()
    t1.goto(pos.x,pos.y)
    t1.dot(20)

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 300:
            speed.y = 0
            pos.y = -250
    
    bird.clear()
    if birdhitted is False :
        birdpos.x -= 0.6
        bird.goto(birdpos.x, birdstarty)
    if(birdpos.x < -250):
        birdpos.x = birdstartx
    if abs(birdpos-pos) < 15:
        birdhitted = True
    if birdhitted is True:
        bird.shape(bird_dead)
        birdspeed.y -= 0.075
        birdpos.move(birdspeed)
        bird.goto(birdpos.x, birdpos.y)
        if(birdpos.y < -250):
            birdhitted = False
            bird.shape(bird_img)
            bird.goto(birdstartx, birdstarty)


    ontimer(draw, 8)

def west():
    pos.x -= 20

def east():
    pos.x += 20

def fire():
    speed.y = 0.000001

pos = vector(0,-250)
speed = vector (0, 0)
tracer(80, 50)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, 'space')

listen()
draw()

exitonclick()