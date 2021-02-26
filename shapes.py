import turtle


def flying_function(self, x, y=None):
    self.up()
    self.goto(x, y)
    self.down()


turtle.Turtle.flyto = flying_function


class Sculptor:
    def __init__(self, turtle_obj):
        self.pen = turtle_obj
        self.screen = turtle.Screen()

    def cross(self, length, color, fill=False):
        self.pen.color(color)
        if fill:
            self.pen.begin_fill()
        for i in range(4):
            self.pen.fd(length)
            self.pen.rt(90)
            self.pen.fd(length)
            self.pen.rt(90)
            self.pen.fd(length)
            self.pen.lt(90)
        if fill:
            self.pen.end_fill()

    def crescent(self, radius, color, fill=False):
        start_heading = self.pen.heading()
        self.pen.color(color)
        if fill:
            self.pen.begin_fill()
        self.pen.rt(120)
        self.pen.circle(radius, 240)
        self.pen.lt(120)
        self.pen.circle(-radius, 120)
        if fill:
            self.pen.end_fill()
        self.pen.seth(start_heading)

    def star(self, side, color, fill=False):
        self.pen.color(color)
        start_heading = self.pen.heading()
        if fill:
            self.pen.begin_fill()
        for i in range(5):
            self.pen.lt(72)
            self.pen.fd(side)
            self.pen.rt(144)
            self.pen.fd(side)
        if fill:
            self.pen.end_fill()
        self.pen.seth(start_heading)

    def trefoil(self, radius, color, fill=False):
        self.pen.color(color)
        start_heading = self.pen.heading()
        if fill:
            self.pen.begin_fill()
        self.pen.circle(-radius, 360*2/3)
        self.pen.lt(120)
        self.pen.circle(-radius, 360*2/3)
        self.pen.lt(120)
        self.pen.circle(-radius, 360*2/3)
        if fill:
            self.pen.end_fill()
        self.pen.seth(start_heading)

    def triangle(self, length, color, fill=False):
        self.pen.color(color)
        start_heading = self.pen.heading()
        if fill:
            self.pen.begin_fill()
        for i in range(3):
            self.pen.fd(length)
            self.pen.lt(120)
        if fill:
            self.pen.end_fill()
        self.pen.seth(start_heading)


"""    def square(self, length):
        for i in range(4):
            self.pen.fd(length)
            self.pen.rt(90)

    def rectangle(self, side_a, side_b):
        for i in range(2):
            self.pen.fd(side_a)
            self.pen.lt(90)
            self.pen.fd(side_b)
            self.pen.lt(90)

    def right_triangle(self, length):
        self.pen.fd(length)
        self.pen.lt(135)
        self.pen.fd((2*(length**2))**(1/2))  # hypotenuse
        self.pen.lt(135)
        self.pen.fd(length)
        self.pen.lt(90)

    def trapeze(self, floor, ceiling, height):
        self.pen.fd(floor)
        self.pen.goto(self.pen.xcor()-(floor-ceiling)/2, self.pen.ycor()+height)
        self.pen.lt(180)
        self.pen.fd(ceiling)
        self.pen.goto(self.pen.xcor()-(floor-ceiling)/2, self.pen.ycor()-height)
        self.pen.lt(180)

    def kite(self, shorter_len, longer_len):
        start_x, start_y = (self.pen.xcor()), (self.pen.ycor())
        self.pen.lt(45)
        self.pen.fd(shorter_len)
        self.pen.rt(90)
        self.pen.fd(shorter_len)
        self.pen.goto(self.pen.xcor()-shorter_len/(2**(1/2)), self.pen.ycor()-(longer_len**2-shorter_len/(2**(1/2))**2)**(1/2))
        self.pen.goto(start_x, start_y)
        self.pen.lt(45)

    def polygon(self, points):
        self.pen.up()
        self.pen.goto(points[0][0], points[0][1])
        self.pen.down()
        for i in range(1, len(points)):
            self.pen.goto(points[i][0], points[i][1])
        self.pen.goto(points[0][0], points[0][1])

    def parallelogram(self, base, side, angle):
        self.pen.fd(base)
        self.pen.lt(180-angle)
        self.pen.fd(side)
        self.pen.lt(angle)
        self.pen.fd(base)
        self.pen.lt(180-angle)
        self.pen.fd(side)
        self.pen.lt(angle)

    def ellipse(self, radius):
        for i in range(2):
            self.pen.circle(radius, 90)
            self.pen.circle(radius//2, 90)

    def semicircle(self, radius):
        self.pen.circle(radius, 180)
        self.pen.lt(90)
        self.pen.fd(radius*2)

    def ring(self, outter_radius, inner_radius):
        self.pen.flyto(self.pen.xcor(), self.pen.ycor()-outter_radius)
        self.pen.circle(outter_radius)
        self.pen.flyto(self.pen.xcor(), self.pen.ycor() + (outter_radius-inner_radius))
        self.pen.circle(inner_radius)
        self.pen.flyto(self.pen.xcor(), self.pen.ycor() - (outter_radius-inner_radius))
        self.pen.flyto(self.pen.xcor(), self.pen.ycor()+outter_radius)

    def pic(self, radius):
        self.pen.rt(90)
        self.pen.circle(-radius, 270)
        self.pen.rt(90)
        self.pen.fd(radius)
        self.pen.lt(90)
        self.pen.fd(radius)

    def flower(self, radius):
        for i in range(4):
            self.pen.lt(90)
            self.pen.circle(radius, 180)

    def quatrefoil(self, radius):
        self.pen.lt(90)
        for i in range(4):
            self.pen.circle(radius, 180)
            self.pen.rt(90)"""