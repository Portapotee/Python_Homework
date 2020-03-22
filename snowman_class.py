class Snowman:
    def __init__(self, bottomX, bottomY, head, body, leg,):
        self.bottomX = bottomX
        self.bottomY = bottomY
        self.head = head
        self.body = body
        self.leg = leg

    def drawBody(self, pen1):
        pen1.pu()
        pen1.goto(self.bottomX, self.bottomY+2*self.leg)
        pen1.down()
        pen1.circle(self.body)
        pen1.pu()
        pen1.goto(self.bottomX,self.bottomY+self.leg*21/8)
        pen1.down()
        pen1.circle(self.body/5)
        pen1.pu()
        pen1.goto(self.bottomX,self.bottomY+self.leg*17/8)
        pen1.down()
        pen1.circle(self.body/5)
        pen1.pu()
        pen1.goto(self.bottomX + self.body,self.bottomY+self.leg*20/8)
        pen1.down()
        pen1.fd(self.body)
        pen1.pu()
        pen1.goto(self.bottomX - self.body,self.bottomY+self.leg*20/8)
        pen1.down()
        pen1.fd(-self.body)

    def drawHead(self, pen1):
        pen1.pu()
        headBottomY = self.bottomY + 2*self.leg+2*self.body
        headBottomX = self.bottomX + self.head*1/4
        pen1.goto(self.bottomX, headBottomY)
        pen1.down()
        pen1.circle(self.head)
        pen1.pu()
        pen1.goto(headBottomX, headBottomY + self.head*3/5)
        pen1.left(30)
        pen1.down()
        pen1.circle(self.head*2/3, -60)
        pen1.left(30)
        pen1.pu()
        pen1.goto(self.bottomX - self.body*1/4,self.bottomY + self.leg*3.45)
        pen1.down()
        pen1.circle(self.head/8)
        pen1.pu()
        pen1.goto(self.bottomX + self.body*1/4,self.bottomY + self.leg*3.45)
        pen1.down()
        pen1.circle(self.head/8)

    def drawLeg(self, pen1):
        pen1.pu()
        pen1.goto(self.bottomX, self.bottomY)
        pen1.down()
        pen1.circle(self.leg)
        pen1.pu()
        pen1.goto(self.bottomX,self.bottomY+self.leg*10/8)
        pen1.down()
        pen1.circle(self.body/4)
        pen1.pu()
        pen1.goto(self.bottomX,self.bottomY+self.leg*4/8)
        pen1.down()
        pen1.circle(self.body/4)


    def draw(self, pen1):
        self.drawLeg(pen1)
        self.drawBody(pen1)
        self.drawHead(pen1)


def drawCircle(pen1, x, y, r):

    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.circle(r)


def drawLine(pen1, x, y, angle, length):

    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.left(angle)
    pen1.fd(length)
    pen1.right(angle)


def drawTriangle(pen1, x, y, side):
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.right(60)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)
    pen1.right(60)


def drawRectangle(pen1, x, y, width, height):
  
    pen1.up()
    pen1.goto(x, y)
    pen1.down()
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)
    pen1.right(90)
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)
    pen1.right(90)