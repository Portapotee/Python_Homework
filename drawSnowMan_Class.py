from turtle import *
from snowman_class import *

pen1 = Turtle()
screen1 = Screen()
pen1.shape("turtle")


man = Snowman(-40, -100, 20, 40, 70)
man.draw(pen1)

kid = Snowman(90, -100, 10, 20, 35)
kid.draw(pen1)

woman = Snowman(-190, -100, 20, 40, 70)
woman.draw(pen1)

kid2 = Snowman(160, -100, 10, 20, 35)
kid2.draw(pen1)

baby = Snowman(230, -100, 5, 10, 17.5)
baby.draw(pen1)

drawLine(pen1, -280, -100, 0, 700)
#pen1.hideturtle()


screen1.mainloop()