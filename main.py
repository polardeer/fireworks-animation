import turtle
import shapes
import random
from fireworks import Firework

# global properties
turtle.delay(0)
turtle.colormode(255)
bg_color = (5, 0, 20)
screen = turtle.Screen()
screen.bgcolor(bg_color)

# main functions definitions


def start_firework(user_x, user_y):
    """Start firework from user_x position, and make it explode on user_y height,
    all other mutable properties of firework are drawn randomly"""
    firework = Firework(FW_MOVER, FW_PAINTER, FW_BASE_YCOR, bg_color)
    r_size = random.randrange(fw_min_size, fw_max_size, fw_size_step)
    r_color = fw_colors[random.randrange(0, len(fw_colors))]
    r_angle = random.randrange(0, 360)
    r_curvature = random.randrange(fw_min_curvature, fw_max_curvature, fw_curvature_step)
    r_shape = fw_shapes[random.randrange(0, len(fw_shapes))]
    firework.start(user_x, user_y, r_size, r_color, r_angle, r_curvature, r_shape)


def start_fireworks_randomly():
    """Start firing off fireworks in a infinite loop,
     all other mutable properties of firework are drawn randomly"""
    while True:
        firework = Firework(FW_MOVER, FW_PAINTER, FW_BASE_YCOR, bg_color)
        r_size = random.randrange(fw_min_size, fw_max_size, fw_size_step)
        r_color = fw_colors[random.randrange(0, len(fw_colors))]
        r_angle = random.randrange(0, 360)
        r_curvature = random.randrange(fw_min_curvature, fw_max_curvature, fw_curvature_step)
        r_shape = fw_shapes[random.randrange(0, len(fw_shapes))]
        r_xcor = random.randrange(fw_min_xcor, fw_max_xcor, fw_xcor_step)
        r_height = random.randrange(fw_min_height, fw_max_height, fw_height_step)
        firework.start(r_xcor, r_height, r_size, r_color, r_angle, r_curvature, r_shape)


"""Parameters for fireworks, fw prefix is a shortcut to firework"""
# turtle pens essential for moving and drawing fireworks
FW_MOVER = turtle.Turtle()
FW_MOVER.hideturtle()
FW_PAINTER = turtle.Turtle()
FW_PAINTER.hideturtle()
# getting shapes from shapes modules
SHAPER = shapes.Sculptor(FW_PAINTER)
# all possible colors
fw_colors = [(255, 102, 0), (255, 74, 46), (255, 213, 0), (230, 255, 0), (255, 0, 94), (255, 0, 20), (255, 255, 0),
             (0, 255, 205), (0, 255, 255), (216, 22, 0), (243, 54, 255)]
fw_shapes = (SHAPER.trefoil, SHAPER.cross, SHAPER.star, SHAPER.crescent, SHAPER.triangle)
number_of_fireworks = 3
FW_BASE_YCOR = -300
# range of x coordinates where fireworks start
fw_min_xcor = -200
fw_max_xcor = 350
fw_xcor_step = 50
# range of possible heights of explosion
fw_min_height = -100
fw_max_height = 250
fw_height_step = 50
# range of possible explosion sizes
fw_min_size = 20
fw_max_size = 45
fw_size_step = 5
# range of possible lift off curvatures
fw_min_curvature = 16
fw_max_curvature = 64
fw_curvature_step = 8

"""Starting program."""
screen.onscreenclick(start_firework)
screen.onkey(start_fireworks_randomly, key='space')
screen.listen()
turtle.mainloop()
turtle.exitonclick()
